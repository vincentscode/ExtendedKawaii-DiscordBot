import discord
from helpers import get_gif

commands = ["needsleep"]
requires_mention = False
accepts_mention = False
description = "Schlaf..! D:"


async def execute(message):
    gif = get_gif('need sleep', platform="tenor", wo_anime=True)

    embed = discord.Embed()
    msg = '{} braucht Schlaf..!'.format(message.author.mention)
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
