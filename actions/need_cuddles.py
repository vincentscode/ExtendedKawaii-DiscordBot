import discord
from helpers import get_gif

commands = ["needcuddles"]
requires_mention = False
accepts_mention = False
description = "Kuscheln..! (｡•́︿•̀｡)"


async def execute(message):
    gif = get_gif('need cuddle', wo_anime=True, lmt=30, pos=0)

    embed = discord.Embed()
    msg = '{} will kuscheln! (｡•́︿•̀｡)'.format(message.author.mention)
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
