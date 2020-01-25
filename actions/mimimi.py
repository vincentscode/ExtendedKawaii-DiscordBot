import discord
from helpers import get_gif

commands = ["mimimi"]
requires_mention = False
accepts_mention = True
description = "MIMIMI (╯°□°)︻╦╤─ - - -"


async def execute(message):
    gif = get_gif('mimimi', wo_anime=True)

    embed = discord.Embed()
    if len(message.mentions) != 0:
        msg = 'Mimimi, {}!'.format(message.mentions[0].mention)
        embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
