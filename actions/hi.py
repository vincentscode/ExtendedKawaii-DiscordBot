commands = ["hi"]
requires_mention = False
accepts_mention = True
description = "Hi! (✿◠‿◠)"


async def execute(message):
    if len(message.mentions) != 0:
        msg = 'Hi {}! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧'.format(message.mentions[0].mention)
    else:
        msg = 'Hi {}! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧'.format(message.author.mention)
    await message.channel.send(msg)
