import discord
import random

commands = ["baum", "kuschelbaum", "tree"]
requires_mention = False
accepts_mention = False
description = "Ein Kuschelbaum! :deciduous_tree: (´｡• ᵕ •｡`)"

picture_urls = [
    "https://media.tenor.com/images/8b8138af2e4d65465c21bc682ed7da2a/tenor.gif"
]


async def execute(message):
    embed = discord.Embed()
    embed.description = "Baum! Raschel! Baumel! Wui! :deciduous_tree: :green_heart: "
    url = random.choice(picture_urls)
    embed.set_footer(text=url)
    embed.set_image(url=url)

    await message.channel.send(embed=embed)
