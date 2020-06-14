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
]


async def execute(message):
    embed = discord.Embed()
    embed.description = "Miep! :hatching_chick: :heart:"
    url = random.choice(picture_urls)
    embed.set_footer(text=url)
    embed.set_image(url=url)

    await message.channel.send(embed=embed)
