import discord
from helpers import get_gif

commands = ["küss", "süß"]
requires_mention = True
accepts_mention = True
description = "Jemanden küssen! (ɔˆ ³ˆ⋆):hearts:(◦’ںˉ◦)"


async def execute(message):
    if len(message.mentions) == 0:
        await message.channel.send('Wen denn? o.O')
        return

    # self check
    if message.mentions[0].mention == message.author.mention:
        msg = 'Haha!'
        await message.channel.send(msg)
        return
    else:
        msg = '{}, du wurdest von {} geküsst'.format(message.mentions[0].mention, message.author.mention)

    # embed
    embed = discord.Embed()
    embed.description = msg

    print("kiss", msg)
    gif = get_gif('kiss')

    # link check
    if message.mentions[0].name == "Link_iene" and message.mentions[0].discriminator == "8415":
        print("is link")
        if message.author.name == "Vincent" and message.author.discriminator == "0212":
            print("is vincent")
        else:
            gif = get_gif('slap')
            embed.description = "Nein."

    # vincent check
    if message.mentions[0].name == "Vincent" and message.mentions[0].discriminator == "0212":
        print("is vincent")
        if message.author.name == "Link_iene" and message.author.discriminator == "8415":
            print("is link")
        else:
            gif = get_gif('slap')
            embed.description = "Nein."

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
