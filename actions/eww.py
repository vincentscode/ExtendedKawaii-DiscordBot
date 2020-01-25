import discord
from helpers import get_gif

commands = ["eww", "bah"]
requires_mention = False
accepts_mention = False
description = "BAH!"


async def execute(message):
    gif = get_gif('eww')

    embed = discord.Embed()
    msg = 'BAH!'
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
