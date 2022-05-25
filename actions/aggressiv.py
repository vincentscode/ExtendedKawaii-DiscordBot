import discord
import requests
import shelve
from helpers import get_gif, parse, dir_path

commands = ["aggressiv", "aggressive"]
requires_mention = False
accepts_mention = True
description = ">:)"


async def execute(message):
    embed = discord.Embed()
    
    embed.description = f"Aggressiver {message.author.mention} >:)"
    shv = shelve.open("aggressive_config.config")
    if str(message.author.id) in shv:
        gif = shv[str(message.author.id)]
        shv.close()
    else:
        shv.close()
        await message.channel.send("Bitte füge zuerst mit `` +setagressive <url> `` ein Bild für deinen +aggressive Befehl hinzu.")
        return

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
