import discord
from helpers import get_islieb, dir_path, parse, print
import asyncio

commands = ["isliebbomb", "comicbomb"]
requires_mention = False
accepts_mention = False
description = "Mehr islieb-comics :eyes:"


async def execute(message):
    gifs = []
    num = 3

    while len(gifs) < num:
        gifs.append(get_islieb())
        gifs = list(set(gifs))

    msg: discord.Message = await message.channel.send('Comic-Bomb - Detonating in 3...')

    await asyncio.sleep(0.4)
    await msg.edit(content="Comic-Bomb - Detonating in 2...")
    await asyncio.sleep(0.4)
    await msg.edit(content="Comic-Bomb - Detonating in 1...")
    await asyncio.sleep(0.4)
    await msg.edit(content="Comic-Bomb - :boom:")

    for gif in gifs:
        file = discord.File(dir_path + "/assets/islieb/" + gif, filename=gif)
        embed = discord.Embed()
        embed.set_image(url="attachment://" + gif)
        await message.channel.send(file=file, embed=embed)

