import discord
from discord.ext import commands
import sys
import os
sys.path.append(os.environ['DB_PATH'])
from db_manager import Database

class LastfmCommands(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.db = Database('d_bot')
        self.db_connection = self.db.connect()
    
    @commands.command()
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

def setup(client):
    client.add_cog(LastfmCommands(client))