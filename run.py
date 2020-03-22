import discord
from discord.ext import commands
import configparser
import os
import sys
import random

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

@client.command()
async def ping(ctx):
    await ctx.send(f'pong {round(client.latency * 1000)} ms')

@client.command()
async def setlastfm(ctx, account_name):
    print(ctx.author)
    print(account_name)
    #await ctx.send('LastFm set!')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["As I see it, yes.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don’t count on it.",
        "It is certain.",
        "It is decidedly so.",
        "Most likely.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Outlook good.",
        "Reply hazy, try again.",
        "Signs point to yes.",
        "Very doubtful.",
        "Without a doubt.",
        "Yes.",
        "Yes – definitely.",
        "You may rely on it."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
    
client.run(token)
