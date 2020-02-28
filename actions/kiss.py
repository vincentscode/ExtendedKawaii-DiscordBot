import discord
from helpers import get_gif

commands = ["küss", "süß"]
requires_mention = True
accepts_mention = True
description = "Jemanden küssen! (ɔˆ ³ˆ⋆):hearts:(◦’ںˉ◦)"


async def execute(message):
    if len(message.mentions) == 0:
        await message.channel.send('Wen denn? o.O')
        return

    if message.mentions[0].mention == message.author.mention:
        await message.channel.send('lol')
        return

    gif = get_gif('kiss')

    embed = discord.Embed()
    embed.description = '{}, du wurdest von {} geküsst'.format(message.mentions[0].mention, message.author.mention)
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
