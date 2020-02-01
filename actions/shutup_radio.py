import discord
import shelve
from helpers import get_gif

commands = ["stfur"]
requires_mention = False
accepts_mention = True
description = "shutup_radio"


async def execute(message):
    embed = discord.Embed()
    if len(message.mentions) != 0:
        msg = 'Shut up, {}!'.format(message.mentions[0].mention)
        if message.mentions[0].name == "keinkreativerNutzername" and message.mentions[0].discriminator == "5012":
            shv = shelve.open("shutup_radio.config")
            if 'lena_counter' in shv:
                shv['lena_counter'] = shv['lena_counter'] + 1
                ctr = int(shv.get('lena_counter'))
            else:
                shv['lena_counter'] = 1
                ctr = 1
            shv.close()

            msg = 'Shut up, {}!\nDu wurdest zum {} Mal mit einem Radio zum schweigen gebracht.'.format(message.mentions[0].mention, ctr)
    else:
        msg = 'Shut up!'
    embed.description = msg
    embed.set_image(url="https://media.tenor.com/images/a3cefe5da142e9ad28dac7d219630696/tenor.gif")

    await message.channel.send(embed=embed)
