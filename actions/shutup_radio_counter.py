import shelve

commands = ["stfurc"]
requires_mention = False
accepts_mention = False
description = "Radios. Viele Radios."


async def execute(message):
    if len(message.mentions) != 0:
        shv = shelve.open("shutup_radio.config")
        if message.mentions[0].id == 545558883431874580:  # Maluka Legacy
            if 'lena_counter' in shv:
                ctr = int(shv.get('lena_counter'))
            else:
                ctr = 0
        else:  # general user id based counter
            if str(message.mentions[0].id) in shv:
                ctr = int(shv.get(str(message.mentions[0].id)))
            else:
                ctr = 0
        shv.close()
        await message.channel.send('{} wurde schon zum {}. Mal mit einem Radio zum schweigen gebracht.'.format(message.mentions[0].mention, ctr))
    else:
        await message.channel.send('Für welchen User?')
