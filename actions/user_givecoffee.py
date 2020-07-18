
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
            embed.description = f"<:metalcoffee:707941148777512966>"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"<:metalcoffee:707941148777512966>"
        else:
            # 0 mentions
            embed.description = f"<:metalcoffee:707941148777512966>"
    else:
        embed.description = f"<:metalcoffee:707941148777512966>"

    embed.set_footer(text="Emote von Metalpig#9228", icon_url="https://cdn.discordapp.com/avatars/184358788260691969/6d78b95237f046b2b249f95f4e91dff6.webp?size=128")
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
