commands = ["ping"]
requires_mention = False
accepts_mention = False
description = "Lebe ich noch? :eyes:"


async def execute(message):
    await message.channel.send("Pong!")
