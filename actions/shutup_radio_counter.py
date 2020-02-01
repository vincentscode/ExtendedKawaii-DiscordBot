import discord
import shelve

commands = ["stfurc"]
requires_mention = False
accepts_mention = False
description = "stfurc"


async def execute(message):
    shv = shelve.open("shutup_radio.config")
    if 'lena_counter' in shv:
        shv['lena_counter'] = shv['lena_counter'] + 1
        ctr = int(shv.get('lena_counter'))
    else:
        shv['lena_counter'] = 1
        ctr = 1
    shv.close()
    print(ctr)
    await message.channel.send('Lena wurde schon zum {} Mal mit einem Radio zum schweigen gebracht.'.format(ctr))
