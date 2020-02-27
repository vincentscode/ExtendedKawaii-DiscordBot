import discord
from helpers import get_gif

commands = ["kissenschlacht", "pillowfight"]
requires_mention = True
accepts_mention = True
description = "Eine Kissenschlacht! <:ishappy:682625825824440353>"


async def execute(message):
    if len(message.mentions) == 0:
        await message.channel.send("Mit wem denn? o.O\n(Bitte gib einen gültigen Nutzer an)")
        return
        
    gif = get_gif('pillow fight')

    embed = discord.Embed()
    if len(message.mentions) == 1:
        # 1 mention
        embed.description = f"{message.author.mention} schlägt {message.mentions[0].mention} mit einem Kissen o.O"
    elif len(message.mentions) > 1:
        # > 1 mentions
        embed.description = f"{message.author.mention} schlägt {', '.join([x.mention for x in message.mentions[:-2]]) + ', ' if len(message.mentions[:-2]) > 0 else ''}{' & '.join([x.mention for x in message.mentions[-2:]])} mit Kissen o.O"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
