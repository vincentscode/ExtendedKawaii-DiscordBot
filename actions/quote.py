import discord
import config
import requests

commands = ["quote", "zitat"]
requires_mention = False
accepts_mention = False
description = "Informatiker Zitate"


async def execute(message):
    e = discord.Embed()

    r = requests.get("https://programming-quotes-api.herokuapp.com/quotes/random/lang/en")
    c_j = r.json()
    c = c_j["en"]
    a = c_j["author"]

    e.description = c
    e.set_footer(text=a)
    await message.channel.send(embed=e)
