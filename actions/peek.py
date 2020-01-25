import discord
from helpers import get_gif

commands = ["peek"]
requires_mention = False
accepts_mention = False
description = ":eyes:"


async def execute(message):
    gif = get_gif('peek', wo_anime=True)

    embed = discord.Embed()
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
