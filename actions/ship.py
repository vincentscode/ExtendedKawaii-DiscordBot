import discord
from helpers import get_gif
import random

commands = ["schiff", "couple"]
requires_mention = True
accepts_mention = True
description = "Menschen ~~verschiffen~~ shippen"


async def execute(message: discord.Message):
    if len(message.mentions) != 2:
        await message.channel.send("Wen denn? o.O\n(Bitte gib zwei gültige Nutzer an)")
        return

    name_a = message.guild.get_member(message.mentions[0].id).display_name
    name_b = message.guild.get_member(message.mentions[1].id).display_name

    ship_name = name_a[:int(len(name_a) / 2)] + name_b[int(len(name_b) / 2):]
    random.seed(message.mentions[0].id+message.mentions[1].id)
    love_calc = random.randint(0, 100)

    e = discord.Embed()
    e.title = ':heart: Lovely Shipping! :heart:'
    e.description = f"Shipping Name: **{ship_name}**\n" \
                    f"Liebe zwischen {name_a} & {name_b}: **{love_calc}%**"

    await message.channel.send(embed=e)
