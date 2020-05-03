
import discord
from helpers import get_gif

commands = ["givecoffee"]
requires_mention = False
accepts_mention = False
description = "givecoffee by Vincent#0212"


async def execute(message):
    gif = get_gif("anime coffee", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"☕"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"☕"
        else:
            # 0 mentions
            embed.description = f"☕"
    else:
        embed.description = f"☕"

    embed.set_footer(text="Ein Befehl von Vincent#0212", icon_url="https://cdn.discordapp.com/avatars/363354366113087491/d9fae1a3efd15458e9d20c6d2a7b0964.webp?size=1024")
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
