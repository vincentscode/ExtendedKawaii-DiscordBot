import discord
from helpers import get_gif

commands = ["fluff", "flausch", "flauschel", "wuschel"]
requires_mention = True
accepts_mention = True
description = "Jemanden flauscheln! ^-^"


async def execute(message):
    if len(message.mentions) == 0:
        await message.channel.send('Wen denn? o.O')
        return
    msg = '{}, du wurdest von {} geflauscht'.format(message.mentions[0].mention, message.author.mention)
    gif = get_gif('headpat')

    embed = discord.Embed()
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
