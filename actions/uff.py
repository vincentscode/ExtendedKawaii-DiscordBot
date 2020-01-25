import discord
from helpers import get_gif

commands = ["uff"]
requires_mention = False
accepts_mention = False
description = "Uff! D:"


async def execute(message):
    gif = get_gif('uff', wo_anime=True)

    embed = discord.Embed()
    msg = '{} ufft..'.format(message.author.mention)
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
