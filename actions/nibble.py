import discord
import random
from helpers import get_gif

commands = ["nibble", "knabber", "anknabber"]
requires_mention = True
accepts_mention = True
description = "Jemanden anknabbern :eyes:"


async def execute(message):
    if len(message.mentions) == 0:
        await message.channel.send('Wen denn? o.O')
        return
    gif = get_gif(random.choice(['nibble', 'cat nibble']), pos=0, lmt=20, wo_anime=True)

    embed = discord.Embed()
    msg = '{}, du wurdest {} angeknabbert'.format(message.mentions[0].mention, message.author.mention)
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
