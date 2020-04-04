import discord
from discord.ext import commands
import sys
import os
sys.path.append(os.environ['DB_PATH'])
from db_manager import Database

class LastfmCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

def setup(client):
    client.add_cog(LastfmCommands(client))

db = Database('d_bot')
conn = db.connect()
print(conn)