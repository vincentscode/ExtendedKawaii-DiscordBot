import discord
from helpers import get_gif

commands = ["giggle"]
requires_mention = False
accepts_mention = False
description = "Hehe"


async def execute(message):
    gif = get_gif('giggle')

    embed = discord.Embed()
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
