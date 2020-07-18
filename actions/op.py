import discord
import config
from helpers import get_gif

commands = ["op"]
requires_mention = False
accepts_mention = False
description = "op"


async def execute(message):
    # discord.Member = message.guild.get_member(message.author.id)

    e = discord.Embed()
    e.title = 'Liste der authorisierten User'

    authorized_ids = [x for x in config.admin_ids]
    server_authorized_ids = [member.id for member in message.guild.members if (member.guild_permissions.administrator or member.guild_permissions.manage_messages or member.guild_permissions.manage_roles) and member.id not in authorized_ids and not member._user.bot]

    e.description = f"**Programmierer**\n<@{authorized_ids[0]}>\n<@{authorized_ids[1]}>\n\n**Trusted Users**\n"
    for id in authorized_ids[2:]:
        e.description += f"<@{id}>\n"

    e.description += f"\n**Server Mods**\n"
    for id in server_authorized_ids:
        e.description += f"<@{id}>\n"
    await message.channel.send(embed=e)
