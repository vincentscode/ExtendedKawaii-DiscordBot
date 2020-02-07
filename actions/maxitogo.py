import config
import discord
import random
from helpers import get_gif, get_maxi, dir_path, parse

commands = ["maxitogo", "sendamaxitogo", "sendmaxitogo", "maxitogo+", "maxitogospecial"]
requires_mention = True
accepts_mention = True
description = "1 Maxi für Nebenbuwu (Mit seltenem Spezial-Maxi o.O)"


async def execute(message):
    if len(message.mentions) < 1 and not config.test_mode:
        await message.channel.send("Für wen den? o.O")
        return

    command, channel, params, mentions, author = parse(message)
    embed = discord.Embed()

    if message.mentions[0].name == "DrWurzeli" and message.mentions[0].discriminator == "2058":
        gif = "https://media.tenor.com/images/7e578d4941d0b674c5f22ea2d03f0476/tenor.gif"
        embed.description = "...wait a minute :eyes:"
        embed.set_image(url=gif)
        await message.channel.send(embed=embed)
        return

    if config.test_mode or (message.mentions[0].name == "Fera" and message.mentions[0].discriminator == "7616"):
        if command == "maxitogo+" or command == "maxitogospecial":
            embed.description = "MaxiToGo Spezial wird geliefert!"
            img = get_maxi()
            file = discord.File(dir_path + "/assets/maxitogo/" + img, filename=img)
            embed.set_image(url="attachment://" + img)
            await message.channel.send(file=file, embed=embed)
            return

        if random.choice([True, True, True, True, True, False]):
            embed.description = "MaxiToGo wird geliefert!"
            gif = get_gif('delivery', wo_anime=True, pos=0, lmt=10)
            gif = random.choice([gif, gif, gif, gif, gif, gif, gif, gif, "https://media.tenor.com/images/95db8481113f44469bde907db890856a/tenor.gif"])
            embed.set_image(url=gif)
            await message.channel.send(embed=embed)
        else:
            embed.description = "MaxiToGo Spezial wird geliefert!"
            img = get_maxi()
            file = discord.File(dir_path + "/assets/maxitogo/" + img, filename=img)
            embed.set_image(url="attachment://" + img)
            await message.channel.send(file=file, embed=embed)
    else:
        gif = get_gif('slap')
        embed.description = "Nein."
        embed.set_image(url=gif)
        await message.channel.send(embed=embed)
