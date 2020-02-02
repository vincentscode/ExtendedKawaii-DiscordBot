import discord
from helpers import get_gif, print

commands = ["purzel", "rollt", "rolling", "rollen"]
requires_mention = False
accepts_mention = True
description = "Rumrollen owo"

blacklist = ["https://media.tenor.com/images/16b7245d1fa155fb3c20bcaaf022213c/tenor.gif", "https://media.tenor.com/images/f4e0a7df7b2ccecb200521e2a4515f7b/tenor.gif"]


async def execute(message):
    params = ('roll', 25, 0, True)
    gif = get_gif(*params)
    while gif in blacklist:
        print("skipping role gif", blacklist.index(gif))
        gif = get_gif(*params)

    embed = discord.Embed()

    if len(message.mentions) == 0:
        msg = '{} rollt durch die Gegend'.format(message.author.mention)
    else:
        msg = '{} rollt gegen {}'.format(message.author.mention, message.mentions[0].mention)
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
