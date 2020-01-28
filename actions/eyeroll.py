import discord
from helpers import get_gif
import random

commands = ["eyeroll", "augenroll"]
requires_mention = False
accepts_mention = False
description = ":rolling_eyes:"


async def execute(message):
    gif = get_gif('eyeroll', pos=random.randint(0, 20), lmt=10)

    embed = discord.Embed()
    embed.description = f"{message.author.mention} rollt mit den Augen :rolling_eyes:"
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
