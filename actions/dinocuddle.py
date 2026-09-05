
import discord
from helpers import get_gif

commands = ["dinocuddle"]
requires_mention = False
accepts_mention = True
description = "dinocuddle"

async def execute(message):
    gif = get_gif("dino cuddle", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} kuschelt {message.mentions[0].mention} <:dinopleading:923670907984167052>"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} kuschelt {', '.join([x.mention for x in message.mentions])} <:dinopleading:923670907984167052>"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} kuschelt mit Dino <:dinopleading:923670907984167052>"
    else:
        embed.description = f"{message.author.mention} kuschelt mit Dino <:dinopleading:923670907984167052>"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
