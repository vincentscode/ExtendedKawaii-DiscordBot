import discord
import requests
import shelve
from helpers import get_gif, parse, dir_path

commands = ["sad", "qwq", "cry"]
requires_mention = False
accepts_mention = True
description = ":("


async def execute(message):
    embed = discord.Embed()
    
    embed.description = f"{message.author.mention} weint qwq"
    shv = shelve.open("sad_config.config")
    gif = None
    if str(message.author.id) in shv:
        gif = shv[str(message.author.id)]
        shv.close()
    else:
        shv.close()
        gif = get_gif('cry', wo_anime=False, pos=0, lmt=25)
        embed.set_footer(text="Du kannst mit \"+setsad <url>\" ein festes Bild für deinen +sad Befehl einstellen.")

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
