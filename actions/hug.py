import discord
from helpers import get_gif, parse

commands = ["umarm", "hug"]
requires_mention = False
accepts_mention = True
description = "<:dinoknuddel:923307479885053952>"


async def execute(message: discord.Message):
    command, channel, params, mentions, author = parse(message)

    embed = discord.Embed()

    if len(message.mentions) == 1 and message.mentions[0].mention == message.author.mention:
        # self mention
        embed.description = f"{message.author.mention} umarmt sich selbst owo"
        gif = get_gif("self hug", wo_anime=True, lmt=25, pos=0)

    elif len(message.mentions) == 1:
        # 1 mention
        embed.description = f"{message.author.mention} umarmt {message.mentions[0].mention} <:dinoknuddel:923307479885053952>"
        gif = get_gif('hug')

    elif len(message.mentions) > 1:
        # > 1 mentions
        embed.description = f"{message.author.mention} umarmt {', '.join([x.mention for x in message.mentions[:-2]]) + ', ' if len(message.mentions[:-2]) > 0 else ''}{' & '.join([x.mention for x in message.mentions[-2:]])} <:dinoknuddel:923307479885053952>"
        gif = get_gif('group hug', lmt=15, pos=0)

    else:
        if message.mention_everyone or len(params) == 1 and params[0] == "alle" or len(params) == 1 and params[0] == "@everyone" or len(params) == 1 and params[0] == "@alle":
            # all mentions
            embed.description = f"{message.author.mention} umarmt alle <:ishappy:441572301167656971>"
            gif = get_gif('group hug', lmt=15, pos=0)
        else:
            # 0 mentions
            embed.description = f"{message.author.mention} umarmt sich selbst owo"
            gif = get_gif("selfhug", lmt=25, pos=0)

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
