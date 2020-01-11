from config import token, prefix
from helpers import print
import actions

import discord

client = discord.Client()


def parse(message: discord.Message):
    split = message.content.split(' ')
    command = split[0][1:]
    channel = message.channel
    params = split[1:]
    mentions = message.mentions
    author = message.author

    return command, channel, params, mentions, author


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not message.content.startswith(prefix) or len(message.content) < 1:
        return

    command, channel, params, mentions, author = parse(message)
    # debug: importlib.reload(actions)
    if command in actions.commands:
        await actions.commands[command](channel, params, mentions, author)


@client.event
async def on_ready():
    print('Started')
    print('Name:', client.user.name)
    print('Id:', client.user.id)

client.run(token)
