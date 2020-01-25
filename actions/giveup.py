import discord
from helpers import get_gif

commands = ["giveup"]
requires_mention = False
accepts_mention = True
description = "qwq"


async def execute(message):
    gif = get_gif('give up')

    embed = discord.Embed()
    msg = '{} gibt auf...'.format(message.author.mention)
    if len(message.mentions) != 0:
        msg = '{} gibt {} auf...'.format(message.author.mention, message.mentions[0].mention)
        if message.author.mention == message.mentions[0].mention:
            await message.channel.send("Nicht aufgeben! D:")
            return
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
