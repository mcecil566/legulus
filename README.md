# legulus
latin for "collector"

Purpose

This repo uses the discord.py library to run a Discord bot with commands to interact with the LastFM API. It's not yet hosted anywhere but locally for testing purposes.

Libraries and external resources
- discord.py
- Basic others (requests, sys, os, configparser, json)
- SQL server (I am useing PostGreSQL for this, running locally)

Set up
- Copy repo
- Set up config/main.ini containing Discord API token, LastFM API token, PostGreSQL server data
- Execute run.py with python
- If "bot is ready" is shown, bot should be working

Status

Check the Zenkit for this project to see the feature backlog.

Current commands
- 'setlastfm' sets LastFM account for Discord user in context
- 'np' requests last 4 songs playing/played including artist, song, and if playing, nowplaying flag

Resources

discord.py - https://discordpy.readthedocs.io/en/latest/
LastFM - https://www.last.fm/api
