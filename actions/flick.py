import random

import discord
from helpers import get_gif

commands = ["flick", "snip", "snap"]
requires_mention = True
accepts_mention = True
description = "*forehead flick*"


async def execute(message):
    if len(message.mentions) == 0:
        await message.channel.send("Wen denn? o.O\n(Bitte gib einen gültigen Nutzer an)")
        return
        
    gif = get_gif(random.choice(['flick forehead', 'anime flick']), pos=0, lmt=15, wo_anime=True)

    embed = discord.Embed()
    if len(message.mentions) == 1:
        # 1 mention
        embed.description = f"{message.author.mention} schnippst {message.mentions[0].mention} gegen die Stirn"
    elif len(message.mentions) > 1:
        # > 1 mentions
        embed.description = f"{message.author.mention} schnippst {', '.join([x.mention for x in message.mentions[:-2]]) + ', ' if len(message.mentions[:-2]) > 0 else ''}{' & '.join([x.mention for x in message.mentions[-2:]])} gegen die Stirn"
            
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
