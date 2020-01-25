import discord
from helpers import get_gif

commands = ["sorry"]
requires_mention = False
accepts_mention = True
description = "Sich entschuldigen"


async def execute(message):
    gif = get_gif('sorry')

    # self check
    if len(message.mentions) != 0:
        if message.mentions[0].mention == message.author.mention:
            print("is self")
            gif = get_gif('slap')
            embed = discord.Embed()
            embed.description = "Stop it, {}! D:".format(message.author.mention)
            embed.set_image(url=gif)
            await message.channel.send(embed=embed)
            return

    embed = discord.Embed()
    if len(message.mentions) != 0:
        embed.description = '{} hat sich bei dir entschuldigt, {}'.format(message.author.mention, message.mentions[0].mention)

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
