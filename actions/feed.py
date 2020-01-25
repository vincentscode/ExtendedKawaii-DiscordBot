import discord
from helpers import get_gif
import random

commands = ["feed", "givefood"]
requires_mention = True
accepts_mention = True
description = "Jemanden füttern :eyes:"


async def execute(message):
    gif = get_gif('feed', lmt=15, pos=0)

    if len(message.mentions) == 0:
        await message.channel.send('Wen denn? o.O')
        return

    msg = '{}, du bekommst Essen von {}! {}'.format(message.mentions[0].mention, message.author.mention, ''.join(random.choices([c for c in '🍔🍟🍕🌭🍿🥞🍳🧈🍞🥐🥨🥯🥖🧀🥪🌮🥗🥙🍖🍗🥩🥟🥠🥡🍘🍙🍚'], k=2)))

    embed = discord.Embed()
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
