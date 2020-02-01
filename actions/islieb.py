# import discord
# from helpers import get_comic

commands = ["islieb"]
requires_mention = False
accepts_mention = False
description = "Coming soon™"


async def execute(message):
    await message.channel.send("Coming soon™")

    # gif = get_comic()
    
    # embed = discord.Embed()
    # embed.set_image(url=gif)
    # await message.channel.send(embed=embed)
