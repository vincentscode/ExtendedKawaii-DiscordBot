import config
import discord
import random
from helpers import get_gif, dir_path, parse

commands = ["vinitogo", "sendavinitogo", "vincenttogo", "vinitogospecial"]
requires_mention = True
accepts_mention = True
description = "1 Vini für Tschotsch (ohnes seltenes Spezial-Vini D:)"


async def execute(message):
    print("vinitogo")
    command, channel, params, mentions, author = parse(message)
    embed = discord.Embed()

    if len(message.mentions) > 0:
        if not (message.mentions[0].name == "Johanna" and message.mentions[0].discriminator == "4636"):
            gif = get_gif('slap')
            embed.description = "Nein."
            embed.set_image(url=gif)
            await message.channel.send(embed=embed)
            return

    if command == "vinitogospecial" or not random.choice([True, True, True, True, True, False]):
        embed.description = "ViniToGo Spezial ist leider aus! :("
        img = get_gif('delivery', wo_anime=True, pos=0, lmt=10)
        embed.set_image(img)
        await message.channel.send(embed=embed)

    else:
        embed.description = "ViniToGo wird geliefert!"
        gif = get_gif('delivery', wo_anime=True, pos=0, lmt=10)
        gif = random.choice([gif, gif, gif, gif, gif, gif, gif, gif, "https://media.tenor.com/images/95db8481113f44469bde907db890856a/tenor.gif"])
        embed.set_image(url=gif)
        await message.channel.send(embed=embed)
