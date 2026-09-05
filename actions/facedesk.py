
import discord
from helpers import get_gif

commands = ["facedesk"]
requires_mention = False
accepts_mention = True
description = "facedesk"

async def execute(message):
    gif = get_gif("facedesk", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} schlägt in anwesenheit von {message.mentions[0].mention} seinen/ihren Kopf auf einen Tisch"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} schlägt in anwesenheit von {', '.join([x.mention for x in message.mentions])} seinen/ihren Kopf auf einen Tisch"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} schlägt seinen/ihren Kopf auf den Tisch"
    else:
        embed.description = f"{message.author.mention} schlägt seinen/ihren Kopf auf den Tisch"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
