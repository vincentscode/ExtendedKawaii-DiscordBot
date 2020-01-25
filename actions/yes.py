import discord
from helpers import get_gif

commands = ["yes", "yup", "ja"]
requires_mention = False
accepts_mention = True
description = "Yes!"


async def execute(message):
    gif = get_gif('yes')

    embed = discord.Embed()
    if len(message.mentions) != 0:
        embed.description = 'Yes, {}'.format(message.mentions[0].mention)
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
