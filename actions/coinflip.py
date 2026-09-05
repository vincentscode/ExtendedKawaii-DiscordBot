import discord
from helpers import get_gif, parse
import random

commands = ["münzwurf", "coinflip"]
requires_mention = False
accepts_mention = False
description = "coinflip"

async def execute(message):
    command, channel, params, mentions, author = parse(message)
    try:
        if len(params) == 0:
            num = random.randint(0, 1)
            if num == 0:
                await message.channel.send("Kopf")
            elif num == 1:
                await message.channel.send("Zahl")
            else:
                await message.channel.send("Fehler: " + str(num))

        elif len(params) >= 2:
            num = random.randint(0, len(params)-1)
            await message.channel.send(params[num])
        else:
            await message.channel.send("Fehler: Falsche Parameteranzahl\nBitte gib >=2 oder keine Optionen an.")
    except Exception as ex:
        await message.channel.send("Fehler: " + str(ex))