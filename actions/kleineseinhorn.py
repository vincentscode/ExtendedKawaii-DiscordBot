import discord
from helpers import get_gif, print

commands = ["kleineseinhorn"]
requires_mention = False
accepts_mention = True
description = "Ein kleines Einhorn 😏"

async def execute(message):
    gif = "https://cdn.discordapp.com/attachments/435791659322703902/731574959381413968/mein-kleines-einhorn.png"

    embed = discord.Embed()

    if len(message.mentions) == 0:
        msg = '{} liebt sein kleines Einhorn!'.format(message.author.mention)
    else:
        msg = '{} liebt {}s kleines Einhorn! 😏'.format(message.author.mention, message.mentions[0].mention)
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
