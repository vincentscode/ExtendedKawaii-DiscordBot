import discord
from helpers import get_gif

commands = ["tickle", "kitzel"]
requires_mention = True
accepts_mention = True
description = "Jemanden kitzeln! :O"


async def execute(message):
    if len(message.mentions) == 0:
        await message.channel.send('Wen denn? o.O')
        return
    msg = '{}, du wirst von {} durchgekitzelt!'.format(message.mentions[0].mention, message.author.mention)
    gif = get_gif('tickle', wo_anime=False)

    embed = discord.Embed()
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
