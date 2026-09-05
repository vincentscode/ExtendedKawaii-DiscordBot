
import discord
from helpers import get_gif

commands = ["wackelalarm"]
requires_mention = False
accepts_mention = True
description = "wackelalarm"

async def execute(message):
    gif = get_gif("shake alarm clock", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} schüttelt {message.mentions[0].mention}s Wecker."
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} schüttelt {', '.join([x.mention for x in message.mentions])}s Wecker."
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} schüttelt den Wecker."
    else:
        embed.description = f"{message.author.mention} schüttelt den Wecker."

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
