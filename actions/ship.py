import discord
from helpers import get_gif

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

    e = discord.Embed()
    e.title = ':heart: Lovely Shipping! :heart:'
    e.description = "Shipping Name: **" + name_a[:int(len(name_a) / 2)] + name_b[int(len(name_b) / 2):] + "**"

    await message.channel.send(embed=e)
