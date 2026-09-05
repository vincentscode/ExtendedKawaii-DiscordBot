import discord
import random

commands = ["baum", "kuschelbaum", "tree"]
requires_mention = False
accepts_mention = False
description = "Ein Kuschelbaum! :deciduous_tree: (´｡• ᵕ •｡`)"

picture_urls = [
    "https://media.tenor.com/images/8b8138af2e4d65465c21bc682ed7da2a/tenor.gif",
    "https://cdn.pixabay.com/photo/2018/03/14/09/49/tree-3224754_960_720.jpg",
    "https://cdn.pixabay.com/photo/2018/03/14/09/49/tree-3224754__480.jpg",
    "https://cdn.pixabay.com/photo/2015/03/26/10/50/green-692079__480.jpg",
    "https://cdn.pixabay.com/photo/2018/01/03/17/05/palm-trees-3058728__480.jpg",
]


async def execute(message):
    embed = discord.Embed()
    embed.description = "Baum! Raschel! Baumel! Wui! :deciduous_tree: :green_heart: "
    url = random.choice(picture_urls)
    embed.set_footer(text="Source: Tenor & Pixabay")
    embed.set_image(url=url)

    await message.channel.send(embed=embed)
