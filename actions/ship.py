import discord
from helpers import get_gif
import random
import math

commands = ["schiff", "couple", "ship"]
requires_mention = True
accepts_mention = True
description = "Menschen ~~verschiffen~~ shippen"

override = {}

async def execute(message: discord.Message):
    if len(message.mentions) < 2:
        await message.channel.send("Wen denn? o.O\n(Bitte gib mindestens zwei gültige Nutzer an)")
        return

    names = [message.guild.get_member(mention.id).display_name for mention in message.mentions]
    ids = [mention.id for mention in message.mentions]
    total_names_length = sum([len(name) for name in names])
    total_names_count = len(names)
    avg_name_length = total_names_length / total_names_count
    contribution_per_name = int(math.ceil(avg_name_length / total_names_count))

    name_a = names[0]
    name_b = names[1]
    ship_name = name_a[:int(len(name_a) / 2)] + name_b[int(len(name_b) / 2):]

    ship_name = ""
    itr = 0
    for name in names:
        start_idx = min([itr, len(name)-contribution_per_name-1])
        ship_name += name[start_idx:start_idx+contribution_per_name]
        itr += contribution_per_name

    random.seed(sum(ids))
    love_calc = random.randint(0, 100)

    extra_over = ""
    love_names_str = " & ".join(names)

    e = discord.Embed()
    e.title = ':heart: Lovely Shipping! :heart:'
    e.description = f"Shipping Name: **{ship_name}**\n" \
                    f"Liebe zwischen {love_names_str}: **{love_calc}%**{extra_over}"

    await message.channel.send(embed=e)
