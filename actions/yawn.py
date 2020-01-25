import discord
from helpers import get_gif

commands = ["yawn", "gähn"]
requires_mention = False
accepts_mention = False
description = "Müdigkeit! D:"


async def execute(message):
    gif = get_gif('yawn', platform="tenor")

    embed = discord.Embed()
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
