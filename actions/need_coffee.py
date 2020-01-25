import discord
from helpers import get_gif

commands = ["needcoffee"]
requires_mention = False
accepts_mention = False
description = "Kaffee..! o.o"


async def execute(message):
    gif = get_gif('need coffee', wo_anime=True)

    embed = discord.Embed()
    msg = '{} braucht Kaffee..! :coffee:'.format(message.author.mention)
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
