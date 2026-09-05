import discord
from helpers import get_gif

commands = ["elghug", "moosehug"]
requires_mention = False
accepts_mention = True
description = "elghug"

async def execute(message):
    gif = "https://c.tenor.com/5RJc_fV5s-MAAAAd/riley-moose.gif"

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{message.author.mention} elchkuschelt {message.mentions[0].mention}! <:dinoknuddel:923307479885053952>"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{message.author.mention} elchkuschelt {', '.join([x.mention for x in message.mentions])}! <:dinoknuddel:923307479885053952>"
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} kuschelt mit einem Elch. owo"
    else:
        embed.description = f"{message.author.mention} kuschelt mit einem Elch. owo"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
