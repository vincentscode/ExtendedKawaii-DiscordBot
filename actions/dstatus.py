import discord
import requests
import demjson
import bs4

commands = ["dstatus", "discord", "discordstatus"]
requires_mention = False
accepts_mention = False
description = "Status von status.discord.com"


dc_headers = {
    'authority': 'discord.statuspage.io',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': '*/*',
    'sec-fetch-dest': 'empty',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'dnt': '1',
    'origin': 'https://status.discord.com',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'referer': 'https://status.discord.com/',
    'accept-language': 'en-DE,en;q=0.9,de-DE;q=0.8,de;q=0.7,en-US;q=0.6',
}

as_headers = {
    'authority': 'xn--allestrungen-9ib.de',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'referer': 'https://www.google.com/',
    'accept-language': 'en-DE,en;q=0.9,de-DE;q=0.8,de;q=0.7,en-US;q=0.6',
    'cookie': '_pubcid=263c3d34-5088-4001-9785-cf8ceb45b732; __cfduid=dc7752171b3ea052d801fd2bc620d770f1582144847',
}

tw_headers = {
    'authority': 'ma.twimg.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'sec-fetch-dest': 'image',
    'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-user': '?1',
    'referer': 'https://mobile.twitter.com/discordapp',
    'accept-language': 'en-DE,en;q=0.9,de-DE;q=0.8,de;q=0.7,en-US;q=0.6',
    'cookie': '_twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCMegdvRwAToMY3NyZl9p%250AZCIlMjg5MTA5NTdlNTcyZjVlODQ3MmNlZWMxYTY4ZDk5NGU6B2lkIiViMzAz%250AMjhlYWIzMDY5ODk5MGMwMGZiMTYzMmMzZmFkZg%253D%253D--36b0ac19bb9426db4c5537a6bd45d15418a83f46; personalization_id="v1_jSBLlkDEj7AxTEUMOEaVvQ=="; guest_id=v1%3A158464938003670844; ct0=be8d9015daa58bf3e58873361001d7a6; eu_cn=1; _mobile_sess=BAh7ByIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNoSGFzaHsABjoKQHVzZWR7ADoQX2NzcmZfdG9rZW4iLThhMTE2OTI1ODRiYWM3ZDMxMjEyNWU4MjBiN2VmMTc4MjI4YTQ5Zjk%3D--4722e5c9c0cc84cfbd89b4b4ef99d8323d7971ca; m5=off; mobile_metrics_token=158464944634524152; d=32',
    'Referer': 'https://mobile.twitter.com/discordapp',
    'Sec-Fetch-Dest': 'image',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'DNT': '1',
}


async def execute(message):
    e = discord.Embed()
    e.set_thumbnail(url="https://discord.com/assets/2c21aeda16de354ba5334551a883b481.png")
    e.set_author(name="Discord Status", url="https://status.discord.com/")

    response = requests.get('https://status.discord.com/api/v2/status.json', headers=dc_headers)
    e.description = "Status: " + response.json()["status"]["description"]

    response = requests.get('https://discord.statuspage.io/metrics-display/ztt4777v23lf/day.json', headers=dc_headers)
    e.add_field(name="Letzter Ping", value=response.json()["summary"]["last"], inline=False)
    e.add_field(name="Durchschnittlicher Ping", value=str(int(response.json()["summary"]["mean"])) + "\n\n\n\n", inline=False)

    #response = requests.get('https://xn--allestrungen-9ib.de/stoerung/discord/', headers=as_headers)
    #rtxt = response.text.replace(" ", "").replace("\n", "").replace("\r", "")

    #idx1 = rtxt.index("<canvas id='holder'></canvas><script type='text/javascript'>// <![CDATA[".replace(" ", ""))
    #rtxt1 = rtxt[idx1:]

    #idx2 = rtxt1.index("$(function(){")
    #rtxt2 = rtxt1[:idx2]

    #idx3 = len("<canvasid='holder'></canvas><scripttype='text/javascript'>//<![CDATA[vardata=")
    #rtxt3 = rtxt2[idx3:].replace("'", "\"")
    #dec = demjson.decode(rtxt3)

    status = {
        "success": ":white_check_mark: Keine Störung bei Discord",
        "warning": ":warning: Möglicherweise Störung bei Discord",
        "danger": ":exclamation: Störung bei Discord",
    }
    #e.add_field(name="allestörungen.de", value=status[dec["status"]], inline=False)

    response = requests.get('https://mobile.twitter.com/discord', headers=tw_headers)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    # main_content > div.timeline > table:nth-child(2) > tbody > tr.tweet-container > td > div.tweet-text
    se = soup.find("td", {"class": "tweet-content"})
    print(se)
    e.add_field(name="Letzter Tweet", value=se.text.replace("\n\n", "\n"), inline=False)

    await message.channel.send(embed=e)
