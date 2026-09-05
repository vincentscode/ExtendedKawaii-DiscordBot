import discord
from helpers import get_gif

commands = ["kuschelüberfall", "überfallkuschel"]
requires_mention = False
accepts_mention = True
description = "kuschelüberfall"


async def execute(message):
    gif = get_gif("cuddle attack", wo_anime=True, lmt=25, pos=0)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} kuschelüberfällt {message.mentions[0].mention}!"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} kuschelüberfällt {', '.join([x.mention for x in message.mentions])}!"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} kuschelüberfällt sich selbst. o.O"
    else:
        embed.description = f"{message.author.mention} kuschelüberfällt sich selbst. o.O"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
