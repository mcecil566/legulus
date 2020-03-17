import discord
from discord.ext import commands
import configparser
import os
import sys

config = configparser.ConfigParser()
config.read(os.environ['D_BOT_CONFIG'] + 'main.ini')

token = config['discord']['token']

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.event
async def on_message(message):
    print(f'{message} sent.')
    
client.run(token)
