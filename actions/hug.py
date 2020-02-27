import discord
from helpers import get_gif

commands = ["umarm"]
requires_mention = False
accepts_mention = True
description = "(づ｡◕‿‿◕｡)づ"


async def execute(message):
    embed = discord.Embed()
    if len(message.mentions) == 1 and message.mentions[0].mention == message.author.mention:
        # self mention
        embed.description = f"{message.author.mention} umarmt sich selbst owo"
        gif = get_gif("self hug", wo_anime=True, lmt=25, pos=0)

    elif len(message.mentions) == 1:
        # 1 mention
        embed.description = f"{message.author.mention} umarmt {message.mentions[0].mention}"
        gif = get_gif('hug')

    elif len(message.mentions) > 1:
        # > 1 mentions
        embed.description = f"{message.author.mention} umarmt {', '.join([x.mention for x in message.mentions[:-2]]) + ', ' if len(message.mentions[:-2]) > 0 else ''}{' & '.join([x.mention for x in message.mentions[-2:]])}"
        gif = get_gif('group hug', lmt=25, pos=0)

    else:
        # 0 mentions
        embed.description = f"{message.author.mention} umarmt sich selbst owo"
        gif = get_gif("selfhug")
            
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
