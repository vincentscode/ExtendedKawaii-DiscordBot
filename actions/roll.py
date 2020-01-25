import discord
from helpers import get_gif

commands = ["purzel", "rollt", "rolling", "rollen"]
requires_mention = False
accepts_mention = True
description = "Rumrollen owo"


async def execute(message):
    gif = get_gif('roll', wo_anime=True, lmt=25, pos=0)

    embed = discord.Embed()

    if len(message.mentions) == 0:
        msg = '{} rollt durch die Gegend'.format(message.author.mention)
    else:
        msg = '{} rollt gegen {}'.format(message.author.mention, message.mentions[0].mention)
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
