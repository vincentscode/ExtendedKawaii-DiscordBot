
import discord
from helpers import get_gif

commands = ["happy", "ishappy"]
requires_mention = False
accepts_mention = True
description = "happy"

async def execute(message):
    gif = get_gif("happy", lmt=25, pos=0, wo_anime=False)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} freut sich für {message.mentions[0].mention} Yay!"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} freut sich für {', '.join([x.mention for x in message.mentions])} Yay!"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} freut sich. Yay!"
    else:
        embed.description = f"{message.author.mention} freut sich. Yay!"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
