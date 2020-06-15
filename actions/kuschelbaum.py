import discord
import random

commands = ["baum", "kuschelbaum", "tree"]
requires_mention = False
accepts_mention = False
description = "Ein Kuschelbaum! :deciduous_tree: (´｡• ᵕ •｡`)"

picture_urls = [
    "https://media.tenor.com/images/8b8138af2e4d65465c21bc682ed7da2a/tenor.gif",
    "https://cdn.discordapp.com/attachments/564034767813738516/722147013814255616/tree-338211__340.png",
    "https://cdn.discordapp.com/attachments/564034767813738516/722146942355767306/tree-1959267__340.png",
    "https://cdn.discordapp.com/attachments/564034767813738516/722146878933827636/tree-407256__340.png",
    "https://cdn.discordapp.com/attachments/564034767813738516/722146800559063070/tree-576847__340.png",
    "https://cdn.discordapp.com/attachments/564034767813738516/722146745106301000/tree-736881__340.png",
    "https://cdn.discordapp.com/attachments/564034767813738516/722146691620536330/fog-3622519__340.png",
    "https://cdn.discordapp.com/attachments/564034767813738516/722147070869241866/tree-1511608__340.png",
    "https://cdn.discordapp.com/attachments/564034767813738516/722147272258748506/cyprus-1990939__340.png",
    "https://cdn.discordapp.com/attachments/564034767813738516/722147337018933368/tree-164915__340.png",
    "https://cdn.discordapp.com/attachments/564034767813738516/722147419503984750/evergreen-2025158__340.png",
    "https://cdn.discordapp.com/attachments/564034767813738516/722147621640208465/atoll-2178747__340.png",
    "https://cdn.discordapp.com/attachments/564034767813738516/722147695396913202/tree-3072431__340.png",
    "https://cdn.discordapp.com/attachments/564034767813738516/722147804738224239/sky-3389832__340.png",
    "https://cdn.pixabay.com/photo/2018/03/14/09/49/tree-3224754_960_720.jpg",
    "https://cdn.pixabay.com/photo/2018/03/14/09/49/tree-3224754__480.jpg",
    "https://cdn.pixabay.com/photo/2015/03/26/10/50/green-692079__480.jpg",
    "https://cdn.pixabay.com/photo/2018/01/03/17/05/palm-trees-3058728__480.jpg",
]


async def execute(message):
    embed = discord.Embed()
    embed.description = "Baum! Raschel! Baumel! Wui! :deciduous_tree: :green_heart: "
    url = random.choice(picture_urls)
    embed.set_footer(text="Source: Tenor & Pixabay")
    embed.set_image(url=url)

    await message.channel.send(embed=embed)
