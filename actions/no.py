import discord
from helpers import get_gif

commands = ["no", "nope", "nein"]
requires_mention = False
accepts_mention = True
description = "No!"


async def execute(message):
    gif = get_gif('no')

    embed = discord.Embed()
    if len(message.mentions) != 0:
        embed.description = 'No, {}'.format(message.mentions[0].mention)
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
