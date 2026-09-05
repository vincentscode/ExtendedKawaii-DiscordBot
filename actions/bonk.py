
import discord

commands = ["bonk"]
requires_mention = False
accepts_mention = False
description = "bonk"

async def execute(message):
    gif = "https://c.tenor.com/TKbDxDPCkegAAAAC/horny-jail-go-to-horny-jail.gif"

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"BONK! <:horny:881224960415252500>"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"BONK! <:horny:881224960415252500>"
        else:
            # 0 mentions
            embed.description = f"BONK! <:horny:881224960415252500>"
    else:
        embed.description = f"BONK! <:horny:881224960415252500>"

    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
