import discord
from helpers import get_gif

commands = ["needfood"]
requires_mention = False
accepts_mention = False
description = "Essen...! D:"


async def execute(message):
    gif = get_gif('need food', wo_anime=True)

    embed = discord.Embed()
    msg = '{} braucht Essen!'.format(message.author.mention)
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
