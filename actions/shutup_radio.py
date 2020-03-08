import discord
import shelve

commands = ["stfur"]
requires_mention = False
accepts_mention = True
description = "Radio - geht ins Ohr, bleibt im Kopf"


async def execute(message):
    embed = discord.Embed()
    if len(message.mentions) != 0:
        shv = shelve.open("shutup_radio.config")
        if message.mentions[0].id == 545558883431874580:  # Maluka Legacy
            if 'lena_counter' in shv:
                shv['lena_counter'] = shv['lena_counter'] + 1
                ctr = int(shv.get('lena_counter'))
            else:
                shv['lena_counter'] = 1
                ctr = 1
        else:  # general user id based counter
            if str(message.mentions[0].id) in shv:
                shv[str(message.mentions[0].id)] = shv[str(message.mentions[0].id)] + 1
                ctr = int(shv.get(str(message.mentions[0].id)))
            else:
                shv[str(message.mentions[0].id)] = 1
                ctr = 1
        shv.close()

        msg = 'Shut up, {}!\nDu wurdest zum {}. Mal mit einem Radio zum schweigen gebracht.'.format(message.mentions[0].mention, ctr)
    else:
        msg = 'Shut up!'
    embed.description = msg
    embed.set_image(url="https://media.tenor.com/images/a3cefe5da142e9ad28dac7d219630696/tenor.gif")

    await message.channel.send(embed=embed)
