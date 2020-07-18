
import discord
from helpers import get_gif

commands = ["eatrice", "rice", "giverice", "reis"]
requires_mention = False
accepts_mention = True
description = "eatrice by Myminechū#8923"


async def execute(message):
    gif = get_gif("anime rice", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} hat {message.mentions[0].mention} Reis gegeben! 🍚"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} hat {', '.join([x.mention for x in message.mentions])} Reis gegeben! 🍚"
        else:
            # 0 mentions
            embed.description = f"🍚"
    else:
        embed.description = f"🍚"

    embed.set_footer(text="Ein Befehl von Myminechū#8923", icon_url="https://cdn.discordapp.com/avatars/262034765622935563/9514faf6ee3c5877ae308aeb7b1d862d.webp?size=1024")
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
