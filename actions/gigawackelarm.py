import discord
import random
from helpers import get_gif

commands = ["gigawackelarm"]
requires_mention = False
accepts_mention = True
description = "*waves fouriouslyer*"


async def execute(message):
	await message.channel.send("<a:wackelarm:721807816221786323>"*9)
