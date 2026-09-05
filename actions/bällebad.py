
import discord
from helpers import get_gif

commands = ["bällebad"]
requires_mention = False
accepts_mention = True
description = "bällebad"

async def execute(message):
    gif = get_gif("ball pit", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} nimmt {message.mentions[0].mention} mit ins Bällebad <:dinohappy:923598640449192057>"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} nimmt {', '.join([x.mention for x in message.mentions])} mit ins Bällebad <:dinohappy:923598640449192057>"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} badet im Bällebad <:dinohappy:923598640449192057>"
    else:
        embed.description = f"{message.author.mention} badet im Bällebad <:dinohappy:923598640449192057>"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
