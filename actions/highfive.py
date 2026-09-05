
import discord
from helpers import get_gif

commands = ["highfive"]
requires_mention = False
accepts_mention = True
description = "highfive"

async def execute(message):
    gif = get_gif("anime highfive", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} gibt {message.mentions[0].mention} ein Highfive!"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} gibt {', '.join([x.mention for x in message.mentions])} ein Highfive!"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} gibts sich selbst ein highfive... :o"
    else:
        embed.description = f"{message.author.mention} gibts sich selbst ein highfive... :o"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
