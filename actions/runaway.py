import discord
from helpers import get_gif

commands = ["runaway"]
requires_mention = False
accepts_mention = True
description = "Nichts wie weg! (˚▽˚’!)/"


async def execute(message):
    gif = get_gif('runaway')
    embed = discord.Embed()
    if len(message.mentions) != 0:
        msg = '{} rennt vor {} weg'.format(message.author.mention, message.mentions[0].mention)
        embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
