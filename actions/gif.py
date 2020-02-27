import discord
from helpers import get_gif, parse

commands = ["gif"]
requires_mention = False
accepts_mention = True
description = "Ein gif o.O"


async def execute(message):
    command, channel, params, mentions, author = parse(message)
    mention_strings = [m.mention for m in mentions]
    actual_params = []
    for param in params:
        if param not in mention_strings:
            actual_params.append(param)
    print("Params", params, "|", mention_strings, "=>", actual_params)

    if len(actual_params) == 0:
        await message.channel.send("Wozu denn? o.O\n(Bitte gib einen Suchterm an)")

    gif = get_gif(' '.join(actual_params), wo_anime=True)

    embed = discord.Embed()
    embed.description = f'Gif zu \"{" ".join(actual_params)}\"'
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
