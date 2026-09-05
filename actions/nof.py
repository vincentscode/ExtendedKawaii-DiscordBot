import discord
from helpers import get_gif, parse

commands = ["nof"]
requires_mention = True
accepts_mention = True
description = "nof nof nof"


async def execute(message):
    command, channel, params, mentions, author = parse(message)

    embed = discord.Embed()
    if len(message.mentions) == 1 and message.mentions[0].mention == message.author.mention:
        # self mention
        await message.channel.send("owo?!")
        return
    elif len(message.mentions) == 1:
        # 1 mention
        embed.description = f"{message.author.mention} noft {message.mentions[0].mention}"
    elif len(message.mentions) > 1:
        # > 1 mentions
        embed.description = f"{message.author.mention} noft {', '.join([x.mention for x in message.mentions[:-2]]) + ', ' if len(message.mentions[:-2]) > 0 else ''}{' & '.join([x.mention for x in message.mentions[-2:]])}"

    else:
        if message.mention_everyone or len(params) == 1 and params[0] == "alle" or len(params) == 1 and params[0] == "everyone" or len(params) == 1 and params[0] == "@alle":
            # all mentions
            embed.description = f"{message.author.mention} noft alle <:dinohappy:923598640449192057>"
        else:
            # 0 mentions
            await message.channel.send("Keiner zum noffen da? D:")
            return

    gif = get_gif('cat cuddle', wo_anime=True)
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
