
import discord
from helpers import get_gif

commands = ["slap"]
requires_mention = False
accepts_mention = True
description = "Jemanden schlagen D:"


async def execute(message):
    but_why = "https://media.tenor.com/images/071c91a60ebb6ab9f150f3edd8f30c30/tenor.gif"
    but_why_txt = "No! God! Please! No!"

    embed = discord.Embed()
    if not message.author.mention in [m.mention for m in message.mentions]:
        if len(message.mentions) == 1:
            # 1 mention
            gif = get_gif("slap", lmt=25, pos=0, wo_anime=False)
            embed.description = f"{message.author.mention} schlägt {message.mentions[0].mention}!"
        elif len(message.mentions) > 1:
            # > 1 mentions
            gif = get_gif("slap", lmt=25, pos=0, wo_anime=False)
            embed.description = f"{message.author.mention} schlägt {', '.join([x.mention for x in message.mentions])}!"
        else:
            # 0 mentions
            gif = but_why
            embed.description = but_why_txt
    else:
        gif = but_why
        embed.description = but_why_txt

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
