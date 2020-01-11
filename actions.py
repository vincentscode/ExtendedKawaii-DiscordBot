from config import tenor_key
from helpers import print
import requests
import random
import discord


def get_gif(search_term, lmt=10, pos=None):
    if pos is None:
        pos = random.randint(0, 20)

    r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&contentfilter=medium&pos=%s" % ('anime ' + search_term, tenor_key, lmt, pos))

    if r.status_code == 200:
        gifs = r.json()
        print([itm["url"] for itm in gifs["results"]])
        return random.choice([itm["media"][0]['gif']["url"] for itm in gifs["results"]])
    else:
        return None


async def hi(channel, params, mentions, author):
    msg = 'Hi {}! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧'.format(author.mention)
    await channel.send(msg)


async def fluff(channel, params, mentions, author):
    msg = '{}, du wurdest von {} geflauscht'.format(mentions[0].mention, author.mention)
    gif = get_gif('headpat')

    embed = discord.Embed()
    embed.description = msg
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def yawn(channel: discord.TextChannel, params, mentions, author):
    gif = get_gif('yawn')

    embed = discord.Embed()
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def mauw(channel, params, mentions, author):
    gif = get_gif('sad')

    embed = discord.Embed()
    embed.set_image(url=gif)
    await channel.send(embed=embed)


async def invite(channel, params, mentions, author):
    link = 'https://discordapp.com/oauth2/authorize?client_id=665549589394227220&response_type=code&scope=bot'
    msg = 'Benutze diesen Link um mich einzuluden (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧\n<{}>'.format(link)
    await channel.send(msg)


async def list_commands(channel, params, mentions, author):
    msg = "**Liste der Befehle**\n"
    msg += "  - hi  \n"
    msg += "  - fluff / flausch / flauschel [someone] \n"
    msg += "  - yawn  \n"
    msg += "  - mauw  \n"
    msg += "  - invite  \n"
    msg += "  - help  \n"
    await channel.send(msg)


commands = {
    'hi': hi,
    'fluff': fluff,
    'flausch': fluff,
    'flauschel': fluff,
    'yawn': yawn,
    'mauw': mauw,
    'invite': invite,
    'help': list_commands
}
