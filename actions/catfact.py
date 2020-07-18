import discord
import config
import requests

commands = ["catfact"]
requires_mention = False
accepts_mention = False
description = "Katzenfakten"


async def execute(message):
    e = discord.Embed()

    r = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1")
    c_j = r.json()
    c = c_j["text"]

    e.description = c
    # e.set_footer(text=a)
    await message.channel.send(embed=e)
