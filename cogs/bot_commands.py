import discord
from discord.ext import commands
import random

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong {round(self.client.latency * 1000)} ms')

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    # @commands.command()
    # async def setlastfm(self, ctx, account_name):
    #     print(ctx.author)
    #     print(account_name)
    #     #await ctx.send('LastFm set!')

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
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

def setup(client):
    client.add_cog(Commands(client))