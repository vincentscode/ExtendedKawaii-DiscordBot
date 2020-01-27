import discord
from helpers import get_gif

commands = ["runinto"]
requires_mention = True
accepts_mention = True
description = "Whoa :O"


async def execute(message):
    if len(message.mentions) == 0:
        await message.channel.send('Wen denn? o.O')
        return

    gif = get_gif('run into', pos=0, lmt=30, wo_anime=True)

    embed = discord.Embed()
    msg = '{} rennt gegen {}'.format(message.author.mention, message.mentions[0].mention)
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
