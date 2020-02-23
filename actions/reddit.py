import discord
import requests
from config import reddit_headers
from helpers import parse, print

commands = ["reddit"]
requires_mention = False
accepts_mention = True
description = "Reddit o.O"


async def execute(message):
    command, channel, params, mentions, author = parse(message)
    mention_strings = [m.mention for m in mentions]
    actual_params = []
    for param in params:
        if param not in mention_strings:
            actual_params.append(param)
    print("Params", params, "|", mention_strings, "=>", actual_params)
    if len(actual_params) == 0:
        await message.channel.send("Aus welchem Sub-Reddit? :O")
        return

    response = requests.get(f'https://www.reddit.com/r/{actual_params[0]}/randomrising.json?obey_over18=true', headers=reddit_headers)
    if response.status_code != 200:
        print("response.status_code != 200")
        await message.channel.send(f"AHHHHHHHHH, IRGENDWAS ist kaputt gegangen! o.O\n(Error Code: RED{response.status_code})")
        return
    try:
        response_json = response.json()
        children = response_json["data"]["children"]
        for c in [x["data"] for x in children]:
            print(c)
            try:
                if c["over_18"] or c["url"] is None or "preview" not in c:
                    print(c["over_18"], "|", c["url"] is None, "|", "preview" not in c)
                    continue
            except Exception as ex:
                print("Exception in if", ex)
                continue
            e = discord.Embed()
            e.title = c["title"]
            if c["selftext"] is not None:
                e.description = c["selftext"]
            img_url = c["preview"]["images"][0]["source"]["url"].replace("&amp;s", "&s")
            e.set_image(url=img_url)
            print(c["permalink"])
            e.url = "https://www.reddit.com/" + c["permalink"]
            e.set_footer(text=f'🔼 {c["ups"]} | 🔽 {c["downs"]} | 💬 {c["num_comments"]}')
            print("=>", img_url)
            await message.channel.send(embed=e)
            return
        await message.channel.send(f"AHHHHHHHHH, IRGENDWAS ist kaputt gegangen! o.O\n(Error Code: RED0NC)")
        return
    except Exception as ex:
        print(str(ex))
        await message.channel.send("AHHHHHHHHH, IRGENDWAS ist kaputt gegangen! o.O\n(Error Code: RED123123)")
        return
