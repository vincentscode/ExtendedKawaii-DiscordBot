import discord
from helpers import get_gif

commands = ["yoda"]
requires_mention = False
accepts_mention = False
description = "Yoda :o"


async def execute(message):
    gif = get_gif('yoda')

    embed = discord.Embed()
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
