import discord
from helpers import get_gif

commands = ["anstups", "stups", "pieks"]
requires_mention = False
accepts_mention = True
description = "poke, poke, poke"


async def execute(message):
    gif = get_gif('poke')

    embed = discord.Embed()
    if len(message.mentions) == 1:
        # 1 mention
        embed.description = f"{message.author.mention} stupst {message.mentions[0].mention} an"
    elif len(message.mentions) > 1:
        # > 1 mentions
        embed.description = f"{message.author.mention} stupst {', '.join([x.mention for x in message.mentions[:-2]]) + ', ' if len(message.mentions[:-2]) > 0 else ''}{' & '.join([x.mention for x in message.mentions[-2:]])} an"
    else:
        # 0 mentions
        embed.description = f"{message.author.mention} stupst sich selbst an :o"
            
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
