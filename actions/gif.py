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
    if "@pos" in actual_params:
        lmt = 1
        pos = int(actual_params[actual_params.index("@pos")+1])
        check_last = False
        actual_params.remove(actual_params[actual_params.index("@pos")+1])
        actual_params.remove("@pos")
        print(actual_params)
    else:
        lmt = 30
        pos = 0
        check_last = True

    gif = get_gif(' '.join(actual_params), wo_anime=True, lmt=lmt, pos=pos, check_last=check_last)

    embed = discord.Embed()
    embed.description = f'Gif zu \"{" ".join(actual_params)}\"{f" @ Position {pos} "if lmt == 1 else ""}'
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
