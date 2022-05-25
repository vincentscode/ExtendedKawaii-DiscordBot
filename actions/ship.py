import discord
from helpers import get_gif
import random
import math

commands = ["schiff", "couple", "ship"]
requires_mention = True
accepts_mention = True
description = "Menschen ~~verschiffen~~ shippen"

override = {
    (484445872177020939, 423157187255336983): 69,
    (423157187255336983, 484445872177020939): 69,

    (170170384203776000, 665307488555630632): 100,
    (665307488555630632, 170170384203776000): 100,

    (435449757192814603, 516348000428359702): 69.42,
    (516348000428359702, 435449757192814603): 69.42,

    (696745969190174750, 758713035728224327): 100,
    (758713035728224327, 696745969190174750): 100,

    (363354366113087491, 538763767962533888): "<:bahhh:892124349736308766>",
    (538763767962533888, 363354366113087491): "<:bahhh:892124349736308766>",

    (186938385040932864, None): 100000,
    (None, 186938385040932864): 100000,
}

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
    for over in override:
        if over[0] == message.mentions[0].id and over[1] == message.mentions[1].id:
            love_calc = override[over]
            extra_over = " (true love™)"
            break
        if (over[0] == None and over[1] == message.mentions[1].id) or (over[0] == message.mentions[0].id and over[1] == None):
            love_calc = override[over]
            extra_over = " (true hotdog™)"
            break

    love_names_str = " & ".join(names)

    e = discord.Embed()
    e.title = ':heart: Lovely Shipping! :heart:'
    e.description = f"Shipping Name: **{ship_name}**\n" \
                    f"Liebe zwischen {love_names_str}: **{love_calc}%**{extra_over}"

    await message.channel.send(embed=e)
