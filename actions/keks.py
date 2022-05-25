import discord
from helpers import get_gif

commands = ["keks", "kekse", "cookies", "cookie"]
requires_mention = False
accepts_mention = True
description = ":cookie:"


async def execute(message):
    if len(message.mentions) == 1 and message.mentions[0].mention == message.author.mention:
        # self mention
        m = f"{message.author.mention} nomst Kekse :cookie:"
    elif len(message.mentions) == 1:
        # 1 mention
        m = f"{message.mentions[0].mention}, du hast Kekse von {message.author.mention} bekommen\n\n(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ :cookie:"
    elif len(message.mentions) > 1:
        # > 1 mentions
        m = f"{', '.join([x.mention for x in message.mentions[:-2]]) + ', ' if len(message.mentions[:-2]) > 0 else ''}{' & '.join([x.mention for x in message.mentions[-2:]])}, ihr habt Kekse von {message.author.mention} bekommen\n\n(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ <:isscookies:443903784268070912>"
    else:
        # 0 mentions
        m = f"{message.author.mention} nomst Kekse :cookie:"

    await message.channel.send(content=m)
