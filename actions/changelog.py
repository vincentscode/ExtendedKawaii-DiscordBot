import requests
import discord
from datetime import datetime

commands = ["changelog"]
requires_mention = False
accepts_mention = False
description = "Der Changelog dieses Bots"


async def execute(message):
    url = f'https://api.github.com/repos/vincentscode/ExtendedKawaii-DiscordBot/commits?per_page=5&page=1'
    r = requests.get(url)
    data = r.json()

    embed = discord.Embed()
    embed.title = 'Changelog'
    embed.description = 'Alle Änderungen unter: https://github.com/vincentscode/ExtendedKawaii-DiscordBot/\n\nDie letzten 5 Änderungen:\n'

    for itm in data:
        c = itm['commit']
        commit_message = c['message']
        sha = c['tree']['sha'][:7]
        url = itm["html_url"]
        time = datetime.strptime(c["author"]["date"], "%Y-%m-%dT%H:%M:%SZ")
        name = c["author"]["name"]

        embed.description += f'[``{time.strftime("%d.%m.%Y, %H:%M")}``]({url}) {commit_message}\n'

    embed.set_footer(text='Ein Bot von Vincent#0212', icon_url='https://avatars0.githubusercontent.com/u/26576880?s=60&v=4')

    await message.channel.send(embed=embed)
