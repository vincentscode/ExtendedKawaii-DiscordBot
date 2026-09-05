commands = ["id", "whoami"]
requires_mention = False
accepts_mention = True
description = "id"


async def execute(message):
    if len(message.mentions) == 0:
        await message.channel.send(message.author.id)
        return
    else:
        ids = [str(x.id) for x in message.mentions]
        await message.channel.send(", ".join(ids))
