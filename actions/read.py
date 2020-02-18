import discord
from helpers import get_gif

commands = ["read"]
requires_mention = False
accepts_mention = True
description = "Lesen! :books:"


async def execute(message):
    gif = get_gif('read', wo_anime=True, pos=0, lmt=25)

    embed = discord.Embed()
    if len(message.mentions) != 0:
        embed.description = '{} liest {} vor :books:'.format(message.author.mention, message.mentions[0].mention)
    else:
        embed.description = '{} liest :books:'.format(message.author.mention)
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
