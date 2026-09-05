
import discord
from helpers import get_gif

commands = ["quetsch", "squeeze", "quetschi"]
requires_mention = False
accepts_mention = True
description = "Quetsch"

async def execute(message):
    gif = get_gif("squeeze", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} zerquetscht {message.mentions[0].mention}. Mörder! Mörder!"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} zerquetscht {', '.join([x.mention for x in message.mentions])}. Mörder! Mörder!"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} quetscht wild herum. Was ein Mörder."
    else:
        embed.description = f"{message.author.mention} quetscht wild herum. Was ein Mörder."

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
