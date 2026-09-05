import discord
from helpers import get_gif, dir_path, parse, print

wackel_d = "<a:dinowavefaster:929876731135918100>"
command_content = {
    "wackeldino": wackel_d,
    "dinowave": wackel_d,
    "wavedino": wackel_d,
    "hektowackeldino": wackel_d * 2,
    "kilowackeldino": wackel_d * 3,
    "megawackeldino": wackel_d * 6,
    "gigawackeldino": wackel_d * 9,
    "terawackeldino": wackel_d * 12,
    "petawackeldino": wackel_d * 15,
    "exawackeldino": wackel_d * 18,
    "zettawackeldino": wackel_d * 21,
    "yottawackeldino": wackel_d * 24,
}
commands = [x for x in command_content]
requires_mention = False
accepts_mention = True
description = "wackeldino"

async def execute(message):
    command, channel, params, mentions, author = parse(message)

    await message.channel.send(command_content[command])
