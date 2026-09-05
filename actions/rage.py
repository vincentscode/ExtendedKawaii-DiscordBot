
import discord
from helpers import get_gif

commands = ["rage"]
requires_mention = False
accepts_mention = True
description = "rage"

async def execute(message):
    gif = get_gif("anime rage", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} rastet wegen {message.mentions[0].mention} aus. 😡"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} rastet wegen {', '.join([x.mention for x in message.mentions])} aus. 😡"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} rastet aus. 💥"
    else:
        embed.description = f"{message.author.mention} rastet aus. 💥"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
