import discord
from helpers import get_gif
import random

commands = ["ban", "banhammer"]
requires_mention = True
accepts_mention = True
description = "BAN! :face_with_symbols_over_mouth:"


async def execute(message):
    if len(message.mentions) == 0:
        await message.channel.send('Wen denn? o.O')
        return

    gif = random.choice([get_gif('thanos snap', pos=0, lmt=5, wo_anime=True), get_gif('banhammer', pos=0, lmt=20, wo_anime=True)])

    embed = discord.Embed()
    if len(message.mentions) != 0:
        embed.description = '{} hat {} gebannt'.format(message.author.mention, message.mentions[0].mention)
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
