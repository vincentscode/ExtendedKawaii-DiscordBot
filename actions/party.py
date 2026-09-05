
import discord
from helpers import get_gif

commands = ["party"]
requires_mention = False
accepts_mention = True
description = "party"

async def execute(message):
    gif = get_gif("party", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} feiert eine party mit {message.mentions[0].mention}"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} feiert eine party mit {', '.join([x.mention for x in message.mentions])}"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} feiert alleine"
    else:
        embed.description = f"{message.author.mention} feiert alleine"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
