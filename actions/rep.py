import discord
import shelve
from datetime import datetime
from helpers import get_gif, parse, dir_path

commands = ["rep"]
requires_mention = True
accepts_mention = True
description = "rep"


def check(author_id):
    last_shv = shelve.open("rep_last_config.config")
    if author_id in last_shv:
        last = datetime.fromtimestamp(last_shv[author_id])
    else:
        last = datetime.fromtimestamp(0)
    last_shv.close()

    now = datetime.now()
    print(last, "=>", now)
    return not (last.year == now.year and last.month == now.month and last.day == now.day)


def update_last_used(author_id):
    last_shv = shelve.open("rep_last_config.config")
    last_shv[author_id] = datetime.timestamp(datetime.now())
    last_shv.close()


def increment_user(recv_id):
    ct_shv = shelve.open("rep_ct_config.config")
    if recv_id in ct_shv:
        ct_shv[recv_id] = ct_shv[recv_id] + 1
    else:
        ct_shv[recv_id] = 1
    ct_shv.close()


def get_user(usr_id):
    ct_shv = shelve.open("rep_ct_config.config")
    if usr_id in ct_shv:
        ct = ct_shv[usr_id]
    else:
        ct = 0
    ct_shv.close()
    return ct


async def execute(message):
    embed = discord.Embed()

    command, channel, params, mentions, author = parse(message)
    mention_strings = [m.mention for m in mentions]
    actual_params = []
    for param in params:
        if param not in mention_strings:
            actual_params.append(param)
    print("Params", params, "|", mention_strings, "=>", actual_params)
    if len(actual_params) == 1 and actual_params[0] == "check":
        if len(message.mentions) > 0:
            embed.description = f":up:  | {message.mentions[0].mention} hat {get_user(str(message.mentions[0].id))} Ansehenspunkt(e)."
        else:
            embed.description = f":up:  | {message.author.mention} hat {get_user(str(message.author.id))} Ansehenspunkt(e)."
        await message.channel.send(embed=embed)
        return

    if len(message.mentions) == 1:
        if message.author.mention == message.mentions[0].mention:
            embed.description = f":up:  | Nope."
            await message.channel.send(embed=embed)
            return

        if check(str(message.author.id)):
            embed.description = f":up:  |  {message.author.mention} hat {message.mentions[0].mention} einen Ansehenspunkt gegeben!"
            update_last_used(str(message.author.id))
            increment_user(str(message.mentions[0].id))
        await message.channel.send(embed=embed)
    elif len(message.mentions) == 0:
        if check(str(message.author.id)):
            embed.description = ":up:  |  Du kannst einen Ansehenspunkt vergeben!"
        else:
            embed.description = ":up:  |  Du kannst in morgen einen weiteren Ansehenspunkt vergeben."

        await message.channel.send(embed=embed)
    elif len(message.mentions) > 1:
        await message.channel.send("Wem denn? o.O\n(Bitte gib einen gültigen Nutzer an)")
