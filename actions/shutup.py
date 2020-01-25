import discord
from helpers import get_gif

commands = ["shutup", "stfu"]
requires_mention = False
accepts_mention = True
description = "shutup"


async def execute(message):
    gif = get_gif('stfu')

    embed = discord.Embed()
    if len(message.mentions) != 0:
        msg = 'Shut up, {}!'.format(message.mentions[0].mention)
    else:
        msg = 'Shut up!'
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
