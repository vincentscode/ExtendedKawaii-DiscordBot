import discord
import os
from helpers import get_goat, dir_path

commands = ["goat"]
requires_mention = False
accepts_mention = True
description = "Eine von {} süßen Ziegen! owo".format(len([g for g in os.listdir(dir_path + '/assets/goats/') if not g.endswith('.mp4') and not g.endswith('.db')]))


async def execute(message):
    gif = get_goat()

    file = discord.File(dir_path + "/assets/goats/" + gif, filename=gif)
    embed = discord.Embed()
    if len(message.mentions) != 0:
        embed.description = 'Eine Ziege für {}!'.format(message.mentions[0].mention)
    embed.set_image(url="attachment://" + gif)
    await message.channel.send(file=file, embed=embed)
