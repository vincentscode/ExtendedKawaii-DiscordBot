import discord
from helpers import get_gif

commands = ["needshower"]
requires_mention = False
accepts_mention = False
description = "Duschen.. :eyes:"


async def execute(message):
    gif = get_gif('need shower', wo_anime=True, lmt=15, pos=0)

    embed = discord.Embed()
    msg = '{} braucht eine Dusche..! :sweat_drops:'.format(message.author.mention)
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
