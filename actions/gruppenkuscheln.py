
import discord
from helpers import get_gif

commands = ["gruppenkuscheln"]
requires_mention = False
accepts_mention = True
description = "gruppenkuscheln"

async def execute(message):
    gif = get_gif("Group cuddle", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} kuschelt {message.mentions[0].mention}"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} kuschelt {', '.join([x.mention for x in message.mentions])}"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} kuschelt alle"
    else:
        embed.description = f"{message.author.mention} kuschelt alle"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
