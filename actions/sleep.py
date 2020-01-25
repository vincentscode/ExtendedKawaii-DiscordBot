import discord
from helpers import get_gif

commands = ["sleep", "fallasleep"]
requires_mention = False
accepts_mention = False
description = "Zu viel Müdigkeit! D:"


async def execute(message):
    gif = get_gif('sleep')

    embed = discord.Embed()
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)