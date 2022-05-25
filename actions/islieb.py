import discord
from helpers import get_islieb, dir_path, parse, print
import os

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

    txt_path = dir_path + "/assets/islieb_txt/" + gif + ".txt"
    tr_path = dir_path + "/assets/islieb_tr/" + gif + ".txt"

    txt = f"<nicht transkribiert (füge Texte mit ``+crowdsource txt {gif}`` hinzu)>"
    tr = f"<nicht übersetzt (füge Übersetzungen mit ``+crowdsource tr {gif}`` hinzu)>"
    
    if os.path.exists(txt_path):
        f = open(txt_path, "r")
        txt = f.read()
        f.close()
    
    if os.path.exists(tr_path):
        f = open(tr_path, "r")
        tr = f.read()
        f.close()

    embed = discord.Embed()
    desc = ""
    if len(message.mentions) != 0:
        desc = 'Ein Comic für {}!'.format(message.mentions[0].mention)
    desc += "\n**Text:**\n" + txt
    desc += "\n**Übersetzung:**\n" + tr

    embed.description = desc
    embed.set_image(url="attachment://" + gif)
    await message.channel.send(file=file, embed=embed)
