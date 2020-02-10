import discord
from helpers import get_gif

commands = ["drinkcoffee"]
requires_mention = False
accepts_mention = False
description = "KAFFEE!!! :coffee:"


async def execute(message):
    gif = get_gif('coffee', lmt=25, pos=0)

    embed = discord.Embed()
    embed.description = ':coffee:'
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
