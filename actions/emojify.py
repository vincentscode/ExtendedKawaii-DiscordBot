import discord
from helpers import get_gif, parse, print

commands = ["emojify"]
requires_mention = False
accepts_mention = False
description = "emojify"

async def execute(message):
    try:
        command, channel, params, mentions, author = parse(message)
        input_str = " ".join(params)

        repl_dict = {
            "!": ":exclamation:",
            "?": ":question:",
            "1": ":one:",
            "2": ":two:",
            "3": ":three:",
            "4": ":four:",
            "5": ":five:",
        }

        output_str = ""
        unknwon_chars = []
        for c in input_str.lower():
            if c in "abcdefghijklmnopqrstuvwxyz":
                output_str += f":regional_indicator_{c}: "
            elif c in repl_dict.keys():
                output_str += f"{repl_dict[c]} "
            elif c in ["\n", " "]:
                output_str += "\n"
            else:
                output_str += " "
                unknwon_chars.append(c)

        if len(unknwon_chars) > 0:
            await message.channel.send(f"Warnung: Nicht umwandelbare Zeichen: {list(set(unknwon_chars))}")
        if len(output_str.strip()) > 0:
            await message.channel.send(output_str)
        else:
            await message.channel.send("Fehler: Keines der Zeichen war umwandelbar.")
    except Exception as ex:
        await message.channel.send("Fehler: " + str(ex))
