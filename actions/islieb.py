import discord
from helpers import get_islieb, dir_path, parse, print

commands = ["islieb", "comic"]
requires_mention = False
accepts_mention = True
description = "Ein islieb-comic / islieb comic suche"


async def execute(message):
    command, channel, params, mentions, author = parse(message)
    mention_strings = [m.mention for m in mentions]
    actual_params = []
    for param in params:
        if param not in mention_strings:
            actual_params.append(param)
    print("Params", params, "|", mention_strings, "=>", actual_params)
    if len(actual_params) == 0:
        gif = get_islieb()
    else:
        gif = get_islieb(' '.join(actual_params))

    file = discord.File(dir_path + "/assets/islieb/" + gif, filename=gif)
    embed = discord.Embed()
    if len(message.mentions) != 0:
        embed.description = 'Eine Comic für {}!'.format(message.mentions[0].mention)
    embed.set_image(url="attachment://" + gif)
    await message.channel.send(file=file, embed=embed)
