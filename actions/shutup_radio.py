import discord
from helpers import get_gif

commands = ["stfur"]
requires_mention = False
accepts_mention = True
description = "shutup_radio"


async def execute(message):
    embed = discord.Embed()
    if len(message.mentions) != 0:
        msg = 'Shut up, {}!'.format(message.mentions[0].mention)
    else:
        msg = 'Shut up!'
    embed.description = msg
    embed.set_image(url="https://media.tenor.com/images/a3cefe5da142e9ad28dac7d219630696/tenor.gif")
    await message.channel.send(embed=embed)
