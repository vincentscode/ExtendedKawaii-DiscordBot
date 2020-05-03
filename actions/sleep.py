import discord
from helpers import get_gif

commands = ["sleep", "fallasleep", "givesleep"]
requires_mention = False
accepts_mention = True
description = "Zu viel Müdigkeit! D:"


async def execute(message):
    gif = get_gif('sleep')

    embed = discord.Embed()
    if len(message.mentions) == 1:
        # 1 mention
        embed.description = f"{message.author.mention} schläft eine Runde für {message.mentions[0].mention} 💤"
    elif len(message.mentions) > 1:
        # > 1 mentions
        embed.description = f"{message.author.mention} schläft eine Runde für {', '.join([x.mention for x in message.mentions[:-2]]) + ', ' if len(message.mentions[:-2]) > 0 else ''}{' & '.join([x.mention for x in message.mentions[-2:]])} 💤"
    else:
        # 0 mentions
        embed.description = f"{message.author.mention} schläft 💤"
            
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
