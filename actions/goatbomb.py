import discord
from helpers import get_goat, dir_path
import asyncio

commands = ["goatbomb"]
requires_mention = False
accepts_mention = False
description = "ZIEGEN! :boom:"


async def execute(message: discord.Message):
    gifs = []
    num = 5

    while len(gifs) < num:
        gifs.append(get_goat())
        gifs = list(set(gifs))

    msg: discord.Message = await message.channel.send('Goat-Bomb - Detonating in 3...')

    await asyncio.sleep(0.4)
    await msg.edit(content="Goat-Bomb - Detonating in 2...")
    await asyncio.sleep(0.4)
    await msg.edit(content="Goat-Bomb - Detonating in 1...")
    await asyncio.sleep(0.4)
    await msg.edit(content="Goat-Bomb - :boom:")

    for gif in gifs:
        file = discord.File(dir_path + "/assets/goats/" + gif, filename=gif)
        embed = discord.Embed()
        embed.set_image(url="attachment://" + gif)
        await message.channel.send(file=file, embed=embed)
