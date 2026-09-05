
import discord
from helpers import get_gif

commands = ["goathug"]
requires_mention = False
accepts_mention = True
description = "goathug"

async def execute(message):
    gif = get_gif("goat hug", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} umarmt {message.mentions[0].mention} und Ziegen."
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} umarmt {', '.join([x.mention for x in message.mentions])} und Ziegen."
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} umarmt Ziegen."
    else:
        embed.description = f"{message.author.mention} umarmt Ziegen."

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
