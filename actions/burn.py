
import discord
from helpers import get_gif

commands = ["burn", "brennen", "onfire", "isonfire"]
requires_mention = False
accepts_mention = True
description = "burn"

async def execute(message):
    gif = get_gif("fire", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.mentions[0].mention} wurde von {message.author.mention} zum brennen gebracht. 🔥  Warum hilft denn keiner?"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{', '.join([x.mention for x in message.mentions])} wurde von {message.author.mention} zum brennen gebracht. 🔥  Warum hilft denn keiner?"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} brennt. 🔥  Warum hilft keiner?"
    else:
        embed.description = f"{message.author.mention} brennt. 🔥  Warum hilft keiner?"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
