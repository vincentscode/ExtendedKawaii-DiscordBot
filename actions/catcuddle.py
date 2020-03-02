import discord
from helpers import get_gif

commands = ["catcuddle", "katzenkuschel"]
requires_mention = True
accepts_mention = True
description = "Kuscheln <:ishappy:441572301167656971>"


async def execute(message):
    if len(message.mentions) == 0:
        await message.channel.send("Mit wem denn? o.O\n(Bitte gib einen gültigen Nutzer an)")
        return
    if len(message.mentions) == 1 and message.mentions[0].mention == message.author.mention:
        await message.channel.send("Du kannst dich selbst umarmen, such dir zum kuscheln eine Decke - das funktioniert so nicht! <:trollface:496805278587551766>")
        return

    gif = get_gif('cat cuddle', wo_anime=True, pos=0, lmt=50)

    embed = discord.Embed()
    if len(message.mentions) == 1:
        # 1 mention
        embed.description = f"{message.author.mention} kuschelt {message.mentions[0].mention}"
    elif len(message.mentions) > 1:
        # > 1 mentions
        embed.description = f"{message.author.mention} kuschelt {', '.join([x.mention for x in message.mentions[:-2]]) + ', ' if len(message.mentions[:-2]) > 0 else ''}{' & '.join([x.mention for x in message.mentions[-2:]])}"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
