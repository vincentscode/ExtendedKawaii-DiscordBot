import discord
import random
from helpers import get_gif

commands = ["wackelarm"]
requires_mention = False
accepts_mention = True
description = "*waves fouriously*"


async def execute(message):
	await message.channel.send(f"<a:wackelarm:721807816221786323>")
