import discord
from helpers import get_gif

commands = ["eat", "nomnom", "noms"]
requires_mention = False
accepts_mention = True
description = "Nom!"


async def execute(message):
    embed = discord.Embed()

    if len(message.mentions) == 1:
        # 1 mention
        gif = get_gif('nom')
        embed.description = f"{message.author.mention} nomst {message.mentions[0].mention}"
    elif len(message.mentions) > 1:
        # > 1 mentions
        gif = get_gif('nom')
        embed.description = f"{message.author.mention} nomst {', '.join([x.mention for x in message.mentions[:-2]]) + ', ' if len(message.mentions[:-2]) > 0 else ''}{' & '.join([x.mention for x in message.mentions[-2:]])}"
    else:
        # 0 mentions
        gif = get_gif('eat')
        embed.description = f"{message.author.mention} nomst"
            
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
