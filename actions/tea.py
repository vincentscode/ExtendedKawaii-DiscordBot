
import discord
from helpers import get_gif

commands = ["tea"]
requires_mention = False
accepts_mention = True
description = "tea"

async def execute(message):
    gif = get_gif("tea", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} macht {message.mentions[0].mention} Tee. 🍵"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} macht {', '.join([x.mention for x in message.mentions])} Tee. 🍵"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} trinkt Tee."
    else:
        embed.description = f"{message.author.mention} trinkt Tee."

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
