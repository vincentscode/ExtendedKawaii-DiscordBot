from config import token, prefix, dev_mode
from helpers import print
import actions

import discord

if dev_mode:
    import importlib

client = discord.Client()


def parse(message: discord.Message):
    split = message.content.split(' ')
    command = split[0][1:]
    channel = message.channel
    params = split[1:]
    mentions = message.mentions
    author = message.author

    return command.lower(), channel, params, mentions, author


@client.event
async def on_guild_join(guild):
    print("Joined guild", guild)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not message.content.startswith(prefix) or len(message.content) < 1:
        return

    command, channel, params, mentions, author = parse(message)
    if dev_mode:
        importlib.reload(actions)
    if command in actions.commands:
        print("Executing", command)
        await actions.commands[command](channel, params, mentions, author)


@client.event
async def on_ready():
    print('Started')
    print('Name:', client.user.name)
    print('Id:', client.user.id)
    print('Current guilds:', client.fetch_guilds())

client.run(token)
