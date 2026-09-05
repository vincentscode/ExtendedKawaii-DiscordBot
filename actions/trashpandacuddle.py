
import discord
from helpers import get_gif

commands = ["trashpandacuddle"]
requires_mention = False
accepts_mention = True
description = "trashpandacuddle"

async def execute(message):
    gif = get_gif("racoon cuddle", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} kuschelt {message.mentions[0].mention} <a:TPpeace:924763249331798097>"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} kuschelt {', '.join([x.mention for x in message.mentions])} <a:TPpeace:924763249331798097>"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} wird zum Trashpanda owo"
    else:
        embed.description = f"{message.author.mention} wird zum Trashpanda owo"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
