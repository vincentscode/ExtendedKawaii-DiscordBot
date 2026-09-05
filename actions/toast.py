
import discord
from helpers import get_gif

commands = ["toast"]
requires_mention = False
accepts_mention = True
description = "toast"

async def execute(message):
    gif = get_gif("toaster", lmt=20, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} gibt {message.mentions[0].mention} Toast! <:metaltoast:707697977375850546>"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} gibt {', '.join([x.mention for x in message.mentions])} Toast! <:metaltoast:707697977375850546>"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} nomst Toast. <:metaltoast:707697977375850546>"
    else:
        embed.description = f"{message.author.mention} nomst Toast. <:metaltoast:707697977375850546>"

    embed.set_footer(text="Emote von Metalpig#9228", icon_url="https://cdn.discordapp.com/avatars/184358788260691969/6d78b95237f046b2b249f95f4e91dff6.webp?size=128")
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
