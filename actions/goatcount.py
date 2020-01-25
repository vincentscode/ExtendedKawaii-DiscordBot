import discord
import os
from helpers import get_goat, dir_path

commands = ["goatcount"]
requires_mention = False
accepts_mention = False
description = "Wie viele süße Ziegen? owo"


async def execute(message):
    msg = '{} süße Ziegen!!!'.format(len([g for g in os.listdir(dir_path + '/assets/goats/') if not g.endswith('.mp4') and not g.endswith('.db')]))
    await message.channel.send(msg)
