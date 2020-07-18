import discord
import requests
import shelve
from helpers import get_gif, parse, dir_path

commands = ["sad", "qwq"]
requires_mention = False
accepts_mention = True
description = ":("


async def execute(message):
    embed = discord.Embed()
    if len(message.mentions) == 1:
        # 1 mention
        embed.description = f"Sad {message.mentions[0].mention} qwq"
        shv = shelve.open("sad_config.config")
        if str(message.mentions[0].id) in shv:
            gif = shv[str(message.mentions[0].id)]
            shv.close()
        else:
            shv.close()
            await message.channel.send(f"{message.mentions[0].mention} muss zuerst mit `` +setsad <url> `` ein Bild für den +sad Befehl hinzufügen.")
            return
    elif len(message.mentions) > 1:
        # > 1 mentions
        await message.channel.send("Dieser Befehl funktioniert nur für einzelne Mentions.")
        return
    else:
        # 0 mentions
        embed.description = f"Sad {message.author.mention} qwq"
        shv = shelve.open("sad_config.config")
        if str(message.author.id) in shv:
            gif = shv[str(message.author.id)]
            shv.close()
        else:
            shv.close()
            await message.channel.send("Bitte füge zuerst mit `` +setsad <url> `` ein Bild für deinen +sad Befehl hinzu.")
            return

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
