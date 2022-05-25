import discord
import asyncio
from helpers import get_gif

commands = ["yodabomb"]
requires_mention = False
accepts_mention = False
description = "Mehr Yoda :O"


async def execute(message):
    gifs = []
    num = 3

    while len(gifs) < num:
        gifs.append(get_gif('yoda', wo_anime=True))
        gifs = list(set(gifs))

    msg: discord.Message = await message.channel.send('Yoda-Bomb - Detonating in 3...')

    await asyncio.sleep(0.4)
    await msg.edit(content="Yoda-Bomb - Detonating in 2...")
    await asyncio.sleep(0.4)
    await msg.edit(content="Yoda-Bomb - Detonating in 1...")
    await asyncio.sleep(0.4)
    await msg.edit(content="Yoda-Bomb - :boom:")

    for gif in gifs:
        embed = discord.Embed()
        embed.set_image(url=gif)
        await message.channel.send(embed=embed)
