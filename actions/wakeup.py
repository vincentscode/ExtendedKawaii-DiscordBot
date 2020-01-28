import discord
from helpers import get_gif

commands = ["wakeup", "icebucket", "mobilize"]
requires_mention = True
accepts_mention = True
description = "Nass. :droplet:"


async def execute(message):
    if len(message.mentions) == 0:
        await message.channel.send('Wen denn? o.O')
        return
    gif = get_gif('icebucket', pos=0, lmt=20)

    embed = discord.Embed()
    embed.description = f"{message.author.mention} \"mobilisiert\" {message.mentions[0].mention}"
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
