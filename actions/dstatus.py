import discord
import requests

commands = ["dstatus", "discord", "discordstatus"]
requires_mention = False
accepts_mention = False
description = "Status von status.discordapp.com"


async def execute(message):
    headers = {
        'authority': 'discord.statuspage.io',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': '*/*',
        'sec-fetch-dest': 'empty',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'dnt': '1',
        'origin': 'https://status.discordapp.com',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'referer': 'https://status.discordapp.com/',
        'accept-language': 'en-DE,en;q=0.9,de-DE;q=0.8,de;q=0.7,en-US;q=0.6',
    }

    e = discord.Embed()
    e.title = "Discord Status"

    response = requests.get('https://status.discordapp.com/api/v2/status.json', headers=headers)
    e.description = "Status: " + response.json()["status"]["description"]

    response = requests.get('https://discord.statuspage.io/metrics-display/ztt4777v23lf/day.json', headers=headers)
    e.add_field(name="Letzter Ping", value=response.json()["summary"]["last"], inline=False)
    e.add_field(name="Durchschnittlicher Ping", value=str(int(response.json()["summary"]["mean"])), inline=False)

    await message.channel.send(embed=e)
