import discord
from helpers import get_gif

commands = ["pat", "patpat"]
requires_mention = True
accepts_mention = True
description = "Jemanden patten!"


async def execute(message):
    if len(message.mentions) == 0:
        await message.channel.send('Wen denn? o.O')
        return
    msg = '{}, you got a pat from {}.'.format(message.mentions[0].mention, message.author.mention)
    gif = get_gif('headpat')

    embed = discord.Embed()
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
