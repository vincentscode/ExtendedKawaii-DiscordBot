import discord
from helpers import get_gif

commands = ["source"]
requires_mention = False
accepts_mention = False
description = "Das bin ich! :D"


async def execute(message):
    link = 'https://github.com/vincentscode/ExtendedKawaii-DiscordBot'
    msg = 'Hinter diesem Link findest du meinen Quellcode (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧\n<{}>'.format(link)
    await message.channel.send(msg)
