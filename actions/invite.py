import discord
from helpers import get_gif

commands = ["invite"]
requires_mention = False
accepts_mention = False
description = "Lad mich ein!"


async def execute(message):
    link = 'https://discordapp.com/oauth2/authorize?client_id=665549589394227220&response_type=code&scope=bot'
    msg = 'Benutze diesen Link um mich einzuluden (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧\n<{}>'.format(link)
    await message.channel.send(msg)
