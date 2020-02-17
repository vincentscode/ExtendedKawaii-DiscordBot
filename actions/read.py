import discord
from helpers import get_gif

commands = ["read"]
requires_mention = False
accepts_mention = False
description = "Lesen! :books:"


async def execute(message):
    gif = get_gif('read', wo_anime=True, pos=0, lmt=25)

    embed = discord.Embed()
    embed.description = '*liest* :books:'
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
