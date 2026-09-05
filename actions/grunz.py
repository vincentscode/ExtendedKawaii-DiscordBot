
import discord
from helpers import get_gif

commands = ["grunz"]
requires_mention = False
accepts_mention = True
description = "Grunz"

async def execute(message):
    gif = get_gif("minipig", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} grunzt {message.mentions[0].mention} an."
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} grunzt {', '.join([x.mention for x in message.mentions])} an."
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} grunzt."
    else:
        embed.description = f"{message.author.mention} grunzt."

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
