import discord
from helpers import get_gif

commands = ["grr", "grrr"]
requires_mention = False
accepts_mention = True
description = "Grrrr (╯°□°)︻╦╤─ - - -"


async def execute(message):
    gif = get_gif('grr')

    embed = discord.Embed()
    if len(message.mentions) != 0:
        msg = '{}, du wurdest von {} angegrrt'.format(message.mentions[0].mention, message.author.mention)
        embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
