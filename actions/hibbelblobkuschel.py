
import discord
from helpers import get_gif

commands = ["hibbelblobkuschel"]
requires_mention = False
accepts_mention = True
description = "hibbelblobkuschel"

async def execute(message):
    gif = "https://media.tenor.com/images/6475a7ca01517139b4adb1151e8b49f1/tenor.gif"

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} hibbelt auf {message.mentions[0].mention} zu und umarmt er/sie/es"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} hibbelt auf {', '.join([x.mention for x in message.mentions])} zu und umarmt er/sie/es"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention}hibbelt und umarmt sich"
    else:
        embed.description = f"{message.author.mention}hibbelt und umarmt sich"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
