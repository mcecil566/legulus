import discord
from discord.ext import commands
import configparser
import os

# list of cogs to be loaded on bot startup
startup_extensions = [
    'bot_commands',
    'bot_events',
    'lastfm_commands']

config = configparser.ConfigParser()
config.read(os.environ['D_BOT_CFG'] + 'main.ini')

token = config['discord']['token']

client = commands.Bot(command_prefix = '.')

@client.command()
async def load(ctx, extension_name):
    try:
        client.load_extension('cogs.' + extension_name)
    except Exception as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension('cogs.' + extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

client.run(token)
