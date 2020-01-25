import discord
from helpers import get_gif

commands = ["mauw"]
requires_mention = False
accepts_mention = False
description = ":("


async def execute(message):
    gif = get_gif('sad')

    embed = discord.Embed()
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
