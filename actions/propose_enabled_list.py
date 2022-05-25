import discord
import os
from helpers import get_gif, parse, check_admin_permissions
import helpers

commands = ["lsprope", "lsenabled", "listenabled"]
requires_mention = False
accepts_mention = False
description = "Erlaubte Befehle auflisten"


async def execute(message):
    dir_path = helpers.dir_path + "/server_actions"
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    dir_path += "/" + str(message.channel.original.guild.id)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    e = discord.Embed()

    itms = []

    enabled_cmds = [x for x in os.listdir(dir_path)]
    for itm in enabled_cmds:
        if not itm.startswith("__"):
            itms.append(['#'.join(itm.split('#')[:2]), '#'.join(itm.split('#')[2:])])
    print(itms)

    e.title = f"Erlaubte Befehle ({len(itms)})"
    i = 0
    for itm in itms:
        i += 1
        if i < 25:
            e.add_field(name=itm[0], value=itm[1][:-3], inline=False)
        else:
            await message.channel.send("list may be incomplete - too many enabled commands.\nuse `+help` to see all commands")
            break
    e.description = "Befehle können von berechtigten Nutzern mit\n``+disablecmd [username]#[0000] [command_name]``\nwieder deaktiviert werden."

    await message.channel.send(embed=e)
