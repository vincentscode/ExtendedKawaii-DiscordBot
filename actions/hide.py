
import discord
from helpers import get_gif

commands = ["hide"]
requires_mention = False
accepts_mention = True
description = "hide"

async def execute(message):
    gif = get_gif("hide", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} versteckt sich vor {message.mentions[0].mention}"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} versteckt sich vor {', '.join([x.mention for x in message.mentions])}"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} versteckt sich."
    else:
        embed.description = f"{message.author.mention} versteckt sich."

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
