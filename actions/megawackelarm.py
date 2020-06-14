import discord
import random
from helpers import get_gif

commands = ["megawackelarm"]
requires_mention = False
accepts_mention = True
description = "*waves fouriouslyer*"


async def execute(message):
	await message.channel.send(f"<a:wackelarm:721807816221786323><a:wackelarm:721807816221786323><a:wackelarm:721807816221786323>")
