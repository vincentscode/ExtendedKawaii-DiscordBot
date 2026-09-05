
import discord
from helpers import get_gif

commands = ["nevergonnagiveyouup", "rickroll", "rick"]
requires_mention = False
accepts_mention = True
description = "rickroll"

async def execute(message):
    gif = get_gif("rickroll", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
