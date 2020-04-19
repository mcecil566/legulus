import discord
from discord.ext import commands
import sys
import os
sys.path.append(os.environ['DB_PATH'])
from db_manager import Database
sys.path.append(os.environ['API_PATH'])
from lastfm import LastFm

class LastfmCommands(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.db = Database('d_bot')
        self.db_connection = self.db.connect()
        self.lastfm = LastFm()
    
    @commands.command()
    # set user lastfm account in postgres database or update if we already
    # have an entry based on user input
    async def setlastfm(self, ctx, lastfm_account_name):
        d_user = str(ctx.author)
        d_user_readable = d_user.split('#')[0]
        d_user_id = str(ctx.author.id)

        if self.db.update_lastfm_account(d_user_id, lastfm_account_name) is not None:
            print('Account updated to: {account_name}'.format(
                account_name=lastfm_account_name
            ))
            
            await ctx.send('Updated LastFm for {discord_account} to {lastfm_account}!'.format(
                discord_account=d_user_readable,
                lastfm_account=lastfm_account_name
            ))

        else:
            self.db.add_account(d_user, d_user_id, lastfm_account_name)
            print('Added account to db: {account_name}'.format(
                account_name=lastfm_account_name
            ))
        
            await ctx.send('Set LastFm for {discord_account} to {lastfm_account}!'.format(
                discord_account=d_user_readable,
                lastfm_account=lastfm_account_name
            ))
    
    @commands.command()
    # now playing, get last 4 songs played, plus metadata
    async def np(self, ctx):
        d_user = str(ctx.author)
        d_user_readable = d_user.split('#')[0]
        d_user_id = str(ctx.author.id)

        # make sure we have a lastfm username
        if self.db.get_lastfm_username(d_user_id) is not None:
            lastfm_username = self.db.get_lastfm_username(d_user_id)
            if self.lastfm.now_playing(lastfm_username) is not None:
                recent_tracks = self.lastfm.now_playing(lastfm_username)
            
                await ctx.send(recent_tracks)
            else:
                await ctx.send('Unable to pull latest tracks :(')

        else:
            await ctx.send('Unable to find LastFm account for {d_user_readable}!'.format(
                d_user_readable=d_user_readable
            ))

        # fm.format_query
        # fm.now_playing
        # ctx.send(result)
        pass

def setup(client):
    client.add_cog(LastfmCommands(client))