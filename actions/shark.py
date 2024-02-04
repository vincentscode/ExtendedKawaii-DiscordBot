import discord
import requests
import re
from helpers import parse, print

commands = ["shark", "hai", "blahaj"]
requires_mention = False
accepts_mention = False
description = "1 shark"


class SharkPost:
    author: str
    description: str
    image_url: str

    def __init__(self, author: str, description: str, image_url: str):
        self.author = author
        self.description = description
        self.image_url = image_url


async def execute(message):
    command, channel, params, mentions, author = parse(message)
    shark = get_shark()

    if shark is None:
        await message.channel.send("Could not acquire shark :(")
    
    e = discord.Embed()
    e.title = shark.description
    e.set_image(url=shark.image_url)
    e.set_footer(text=shark.author)
    await message.channel.send(embed=e)


def get_shark() -> SharkPost:
    r = requests.get("https://blahaj.transgirl.dev/images/random")
    if r.status_code != 200:
        return None
    
    j = r.json()

    author = j["author"]
    description = re.findall('\\"(.+)\\" \(.*\)', j["description"])[0]
    url = j["url"]

    return SharkPost(author, description, url)
