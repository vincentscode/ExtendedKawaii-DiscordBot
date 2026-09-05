import discord
from helpers import get_gif

commands = ["bedbring", "bedget"]
requires_mention = False
accepts_mention = True
description = "bedbring"


async def execute(message):
    gif = get_gif("bed", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} bringt {message.mentions[0].mention} ein Bett 🛏️"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} bringt {', '.join([x.mention for x in message.mentions])} ein Bett 🛏️😏"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} holt sich ein Bett 🛏️"
    else:
        embed.description = f"{message.author.mention} holt sich ein Bett 🛏️"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
