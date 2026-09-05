
import discord
from helpers import get_gif

commands = ["indieheiakuschel", "heiakuschel", "idhk"]
requires_mention = False
accepts_mention = True
description = "indieheiakuschel"

async def execute(message):
    gif = get_gif("cuddle")

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} kuschelt sich mit {message.mentions[0].mention} in die Heia."
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} kuschelt sich mit {', '.join([x.mention for x in message.mentions])} in die Heia."
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} kuschelt sich in die Heia."
    else:
        embed.description = f"{message.author.mention} kuschelt sich in die Heia."

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
