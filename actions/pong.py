
commands = ["pong", "🏓"]
requires_mention = False
accepts_mention = False
description = "🏓"


async def execute(message):
    await message.channel.send("Ping!")