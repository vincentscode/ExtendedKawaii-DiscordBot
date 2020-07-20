import discord
import random
from helpers import get_gif
from helpers import check_admin_permissions, parse

prefix = {
    "yotta": 24,
    "zetta": 21,
    "exa": 18,
    "peta": 15,
    "tera": 12,
    "giga": 9,
    "mega": 6,
    "kilo": 3,
    "": 1,
}

commands = [x + "wackelarm" for x in prefix]
requires_mention = False
accepts_mention = False
description = "*waves fouriously*"


async def execute(message):
    print(commands)
    command, channel, params, mentions, author = parse(message)
    c = 1
    for k in prefix:
        if command == k + "wackelarm":
            c = prefix[k]
            break

    await message.channel.send(c*"<a:wackelarm:721807816221786323>")
