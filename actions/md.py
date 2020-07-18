commands = ["md", "markdown"]
requires_mention = False
accepts_mention = False
description = "How to MD"


async def execute(message):
    msg = ""
    msg += "__**Markdown**__\n\n"
    msg += "``*Nachricht*`` => *Nachricht*\n"
    msg += "``**Nachricht**`` => **Nachricht**\n"
    msg += "``__Nachricht__`` => __Nachricht__\n"
    msg += "\nDie Symbole können auch kombiniert werden um zum Beispiel unterstrichenen & kursiven Text zu erzeugen"
    await message.channel.send(msg)
