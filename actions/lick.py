import discord
from helpers import get_gif, get_maxi, dir_path, parse

commands = ["lick", "leck", "anschlabber"]
requires_mention = True
accepts_mention = True
description = "Jemanden anlecken! :eyes:"


async def execute(message):
    if len(message.mentions) == 0:
        await message.channel.send('Wen denn? o.O')
        return

    command, channel, params, mentions, author = parse(message)

    msg = '{}, du wirst von {} (an)geleckt. 😋'.format(message.mentions[0].mention, message.author.mention)

    if command == "anschlabber":
        gif = get_gif('lick', wo_anime=True)
    else:
        gif = get_gif('cat lick', wo_anime=True)

    embed = discord.Embed()
    embed.description = msg
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
