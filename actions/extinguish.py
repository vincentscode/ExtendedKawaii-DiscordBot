import random
import discord
from helpers import get_gif

commands = ["extinguish", "lösch", "löschen"]
requires_mention = False
accepts_mention = True
description = "extinguish"

async def execute(message):
    gif = get_gif(random.choice(["extinguish", "fire brigade"]), lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.mentions[0].mention} wird von {message.author.mention} gelöscht."
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{', '.join([x.mention for x in message.mentions])} wird von {message.author.mention} gelöscht."
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} löscht sich selber. 🧯"
    else:
        embed.description = f"{message.author.mention} löscht sich selber. 🧯"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
