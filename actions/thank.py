import discord
from helpers import get_gif

commands = ["thanks", "thank", "danke"]
requires_mention = False
accepts_mention = True
description = "Sich bedanken owo"


async def execute(message):
    gif = get_gif('thank', wo_anime=True)

    embed = discord.Embed()
    if len(message.mentions) == 1:
        # 1 mention
        embed.description = f"Danke, {message.mentions[0].mention}! <:dinoknuddel:923307479885053952>"
    elif len(message.mentions) > 1:
        # > 1 mentions
        embed.description = f"Danke, {', '.join([x.mention for x in message.mentions[:-2]]) + ', ' if len(message.mentions[:-2]) > 0 else ''}{' & '.join([x.mention for x in message.mentions[-2:]])}! <:dinoknuddel:923307479885053952>"
    else:
        # 0 mentions
        embed.description = "Danke! <:dinoknuddel:923307479885053952>"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
