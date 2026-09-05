import discord

commands = ["reverse"]
requires_mention = False
accepts_mention = False
description = "O: !esrever"


async def execute(message):
    await message.channel.send(message.content[len("+reverse"):].strip()[::-1])
