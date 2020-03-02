import discord
from helpers import get_gif

commands = ["credits"]
requires_mention = False
accepts_mention = False
description = "credits"


async def execute(message):
    if len(message.mentions) > 0:
        await message.channel.send(content=f":credit_card:  |  **{message.guild.get_member(message.mentions[0].id).display_name}** has a balance of :yen: **all** credits!")
    else:
        await message.channel.send(content=f":credit_card:  |  **{message.guild.get_member(message.author.id).display_name}**, you have a balance of :yen: **all** credits!")

