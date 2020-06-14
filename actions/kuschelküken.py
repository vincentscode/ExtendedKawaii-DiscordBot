import discord
import random

commands = ["cuddlechick", "kuschelküken"]
requires_mention = False
accepts_mention = False
description = "Ein Kuschelküken! (´｡• ᵕ •｡`)"

picture_urls = [
    "https://media.tenor.com/images/d47a415586e26da144f95799434ddc59/tenor.gif",
    "https://media.tenor.com/images/45c63edfe068b320698f6aa8317abb06/tenor.gif",
    "https://media.tenor.com/images/786b81c44e33aaed52b94d5481351be2/tenor.gif",
    "https://media.tenor.com/images/bf81564ae058991178057dbf04e4a691/tenor.gif",
    "https://media.tenor.com/images/d0e9f6ccd57fbcaa99c1eafb2e83061d/tenor.gif",
    "https://media.tenor.com/images/fa97254d32837abb671d099394da7395/tenor.gif",
    "https://media.tenor.com/images/cbbe34e6ddc0c6fc523f461139b8daca/tenor.gif",
    "https://media.tenor.com/images/d39006b4093d755a9e0d777e7908274e/tenor.gif",
    "https://media.tenor.com/images/a272eb6bda70b2e76f5f75e3a10798b8/tenor.gif",
    "https://media.tenor.com/images/30accf0f006d16e472c4e49100165e8a/tenor.gif",
    "https://media.tenor.com/images/185933592fa3740cf7029713a30e8c57/tenor.gif",
]


async def execute(message):
    embed = discord.Embed()
    embed.description = "Miep! :hatching_chick: :heart:"
    url = random.choice(picture_urls)
    embed.set_footer(text=url)
    embed.set_image(url=url)

    await message.channel.send(embed=embed)
