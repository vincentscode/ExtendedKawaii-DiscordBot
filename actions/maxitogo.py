import discord
from helpers import get_gif

commands = ["maxitogo", "sendamaxitogo", "sendmaxitogo"]
requires_mention = True
accepts_mention = True
description = "1 Maxi für Nebenbuwu"


async def execute(message):
    gif = get_gif('delivery', wo_anime=True, pos=0, lmt=10)
    if len(message.mentions) < 1:
        return

    embed = discord.Embed()
    if message.mentions[0].name == "Fera" and message.mentions[0].discriminator == "7616":
        print("is fera")
        embed.description = "MaxiToGo wird geliefert!"
    else:
        gif = get_gif('slap')
        embed.description = "Nein."

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
