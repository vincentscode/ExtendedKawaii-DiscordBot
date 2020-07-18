import discord
import random
from helpers import get_gif

commands = ["miau", "meow", "mau"]
requires_mention = False
accepts_mention = True
description = "=(^_^)="


async def execute(message):
    gif = get_gif(random.choice(['cat', 'meow']), platform="tenor")

    if len(message.mentions) == 0:
        msg = '{} miaut'.format(message.author.mention)
    else:
        msg = '{} miaut {} an'.format(message.author.mention, message.mentions[0].mention)

    embed = discord.Embed()
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
