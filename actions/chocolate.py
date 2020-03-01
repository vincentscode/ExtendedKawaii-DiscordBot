import discord
from helpers import get_gif

commands = ["schoki", "givechocolate", "chocolate"]
requires_mention = False
accepts_mention = True
description = "chocolate"


async def execute(message):
    if len(message.mentions) == 1 and message.mentions[0].mention == message.author.mention:
        # self mention
        m = f"{message.author.mention} nomst Schokolade :chocolate_bar:"
    elif len(message.mentions) == 1:
        # 1 mention
        m = f"{message.mentions[0].mention}, du hast Schokolade von {message.author.mention} bekommen\n\n(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ :chocolate_bar:"
    elif len(message.mentions) > 1:
        # > 1 mentions
        m = f"{', '.join([x.mention for x in message.mentions[:-2]]) + ', ' if len(message.mentions[:-2]) > 0 else ''}{' & '.join([x.mention for x in message.mentions[-2:]])}, ihr habt Schokolade von {message.author.mention} bekommen\n\n(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ :chocolate_bar:"
    else:
        # 0 mentions
        m = f"{message.author.mention} nomst Schokolade :chocolate_bar:"

    await message.channel.send(content=m)
