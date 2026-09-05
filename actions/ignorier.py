
import discord
from helpers import get_gif

commands = ["ignorier"]
requires_mention = False
accepts_mention = True
description = "ignorier"

async def execute(message):
    gif = get_gif("ignore", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} ignoriert {message.mentions[0].mention}. Pech gehabt."
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} ignoriert {', '.join([x.mention for x in message.mentions])}. Pech gehabt."
        else:
            # 0 mentions
            embed.description = f"{message.author.mention}, ignorierst du die Luft?"
    else:
        embed.description = f"{message.author.mention}, ignorierst du die Luft?"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
