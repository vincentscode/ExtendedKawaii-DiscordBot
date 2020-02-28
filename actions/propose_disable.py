import discord
from helpers import check_admin_permissions, parse
import helpers
import os
import re
import shutil

commands = ["disablecmd"]
requires_mention = False
accepts_mention = False
description = "Erlaubte befehle deaktivieren"


async def execute(message):
    if not await check_admin_permissions(message):
        return

    # [username]#[0000] command_name
    command, channel, params, mentions, author = parse(message)

    if len(params) != 2:
        await message.channel.send("Fehler: Falsche Parameteranzahl\nBitte verwende die Syntax ``+disablecmd [username]#[0000] [command_name]``")
        return

    save_p0 = re.sub(r'[\\/*?:"<>|]', '', params[0])
    save_p1 = re.sub(r'[\\/*?:"<>|]', '', params[1])
    f_path = helpers.dir_path + "/server_actions/" + str(message.channel.original.guild.id) + "/" + save_p0 + "#" + save_p1 + ".py"
    print(f_path)

    if not os.path.exists(f_path) or not os.path.isfile(f_path):
        await message.channel.send("Fehler: Befehl nicht gefunden\nBitte verwende die Syntax ``+disablecmd [username]#[0000] [command_name]``")
        return

    dir_path = helpers.dir_path + "/server_proposed_actions"
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    dir_path += "/" + str(message.channel.original.guild.id)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    f_dest_path = helpers.dir_path + "/server_proposed_actions/" + str(message.channel.original.guild.id) + "/" + save_p0 + "/" + save_p1 + ".py"
    shutil.move(f_path, f_dest_path)

    await message.channel.send("Server-Befehl erfolgreich deaktiviert\nEr kann mit ``+enablecmd [username]#[0000] [command_name]`` wieder aktiviert werden")
