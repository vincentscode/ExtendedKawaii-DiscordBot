
import discord
from helpers import get_gif

commands = ["schippe", "schüppe", "klönk"]
requires_mention = False
accepts_mention = True
description = "schippe"

async def execute(message):
    gif = get_gif("shovel slap", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} klönkt {message.mentions[0].mention} mit der grünen Plastikschaufel eins über owo"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} klönkt {', '.join([x.mention for x in message.mentions])} mit der grünen Plastikschaufel eins über owo"
        else:
            # 0 mentions
            embed.description = f"KLÖNK <:shovel:873909295379533884>"
    else:
        embed.description = f"KLÖNK <:shovel:873909295379533884>"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
