import discord
import requests
import shelve
from helpers import get_gif, parse, dir_path

commands = ["setaggressive", "setaggressiv"]
requires_mention = False
accepts_mention = False
description = "Set aggressive command image"


# noinspection PyBroadException
def is_url_image(image_url):
    try:
        image_formats = ("image/png", "image/jpeg", "image/jpg", "image/gif")
        r = requests.head(image_url)
        if r.headers["content-type"] in image_formats:
            return True
        return False
    except Exception:
        return False


async def execute(message):
    command, channel, params, mentions, author = parse(message)
    mention_strings = [m.mention for m in mentions]
    actual_params = []
    for param in params:
        if param not in mention_strings:
            actual_params.append(param)
    print("Params", params, "|", mention_strings, "=>", actual_params)

    if len(actual_params) == 0:
        await message.channel.send("Bitte gib eine URL an.")
        return
    if len(actual_params) > 1:
        await message.channel.send("Bitte gib nur eine URL an.")
        return

    if not is_url_image(actual_params[0]):
        await message.channel.send("Die gewählte URL scheint nicht zu existieren oder kein Bild zu sein.")
        return

    shv = shelve.open("aggressive_config.config")
    shv[str(message.author.id)] = actual_params[0]
    shv.close()

    await message.channel.send("+aggressive bild auf <" + actual_params[0] + "> gesetzt.")
