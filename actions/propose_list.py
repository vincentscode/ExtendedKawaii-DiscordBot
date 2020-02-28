import discord
import os
from helpers import get_gif, parse, check_admin_permissions
import helpers

commands = ["lsprop", "listprops", "propose_list"]
requires_mention = False
accepts_mention = False
description = "Angefragte Befehle auflisten"


async def execute(message):
    dir_path = helpers.dir_path + "/server_proposed_actions"
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    dir_path += "/" + str(message.channel.original.guild.id)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    e = discord.Embed()

    itms = []

    proposal_users = [(x, os.path.join(dir_path, x)) for x in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, x))]
    for user_dir in proposal_users:
        user_cmds = os.listdir(user_dir[1])
        # print(user_dir[0], user_cmds)
        for user_cmd in user_cmds:
            itms.append([user_dir[0], user_cmd])

    e.title = f"Angrefragte Befehle ({len(itms)})"
    i = 0
    for itm in itms:
        i += 1
        if i < 25:
            e.add_field(name=itm[0], value=itm[1][:-3], inline=False)
    e.description = "Befehle können von berechtigten Nutzern mit\n``+enablecmd [username]#[0000] [command_name]``\nfreigegeben werden."

    await message.channel.send(embed=e)
