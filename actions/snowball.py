
import discord
from helpers import get_gif

commands = ["snowball"]
requires_mention = False
accepts_mention = True
description = "snowball"

async def execute(message):
    gif = get_gif("snowball anime", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} wirft {message.mentions[0].mention} mit Schneebällen ab! In Deckung! D:"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} wirft {', '.join([x.mention for x in message.mentions])} mit Schneebällen ab! In Deckung! D:"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} wirft mit Schneebällen um sich! :O"
    else:
        embed.description = f"{message.author.mention} wirft mit Schneebällen um sich! :O"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
