
import discord
from helpers import get_gif

commands = ["nice", "approved", "thumbsup"]
requires_mention = False
accepts_mention = True
description = "nice"

async def execute(message):
    gif = get_gif("approved", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} gefällt was {message.mentions[0].mention} tut."
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} gefällt was {', '.join([x.mention for x in message.mentions])} tut."
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} gefällt das."
    else:
        embed.description = f"{message.author.mention} gefällt das."

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
