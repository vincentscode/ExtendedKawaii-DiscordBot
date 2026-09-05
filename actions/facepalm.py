
import discord
from helpers import get_gif

commands = ["facepalm"]
requires_mention = False
accepts_mention = True
description = "facepalm"

async def execute(message):
    gif = get_gif("facepalm", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} schlägt wegen {message.mentions[0].mention} die Hand vor den Kopf"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} schlägt wegen {', '.join([x.mention for x in message.mentions])} die Hand vor den Kopf"
        else:
            # 0 mentions
            embed.description = f"schlägt die Hand vor den Kopf"
    else:
        embed.description = f"schlägt die Hand vor den Kopf"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
