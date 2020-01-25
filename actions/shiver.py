import discord
from helpers import get_gif

commands = ["shiver"]
requires_mention = False
accepts_mention = False
description = "Kalt! D:"


async def execute(message):
    gif = get_gif('shiver')

    embed = discord.Embed()
    msg = '{} zittert.'.format(message.author.mention)
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
