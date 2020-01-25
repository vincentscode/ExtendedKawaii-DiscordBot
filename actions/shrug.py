import discord
from helpers import get_gif

commands = ["shrug"]
requires_mention = False
accepts_mention = False
description = "¯\\_(ツ)_/¯"


async def execute(message):
    gif = get_gif('shrug')

    embed = discord.Embed()
    msg = '{} zuckt mit den Schultern..'.format(message.author.mention)
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
