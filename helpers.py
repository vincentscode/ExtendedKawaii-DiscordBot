import random
from datetime import datetime
import builtins
import os
import discord
from fuzzywuzzy import process
from colorama import Fore
import requests
import config
import importlib.util

from config import tenor_key, giphy_key

last_gif = None
platforms = platforms_with_local = ["tenor"]


dir_path = os.path.dirname(os.path.realpath(__file__))
if not os.path.exists(dir_path + '/logs'):
    os.mkdir(dir_path + '/logs')
log_file = open(dir_path + "/logs/log_{}.txt".format(datetime.now().strftime('%H_%M_%S_%d_%m_%Y')), "w", encoding="utf8")


# noinspection PyShadowingBuiltins
def print(*args, log_level=0, end="\n"):
    if log_level == 0:
        log_prefix = f"{Fore.LIGHTGREEN_EX}INFO {Fore.RESET}"
    elif log_level == 1:
        log_prefix = f"{Fore.YELLOW}WARN {Fore.RESET}"
    elif log_level == 2:
        log_prefix = f"{Fore.RED}ERROR {Fore.RESET}"
    else:
        log_prefix = "     "

    log_prefix = "[" + log_prefix + "] "
    print_string = f"[{Fore.WHITE}" + datetime.now().strftime('%H:%M:%S.%f') + f"{Fore.RESET}] " + log_prefix + " ".join(map(str, args)).replace("\n", "")

    builtins.print(print_string, end=end)
    log_file.write(print_string + end)
    log_file.flush()


async def check_admin_permissions(message):
    if message.author._user.id not in config.admin_ids:
        e = discord.Embed()
        e.title = '❗ Fehler'
        e.description = "Du hast nicht die erforderlichen Berechtigungen um diesen Befehl zu benutzen.\n" \
                        "Wenn du denkst, dass du diesen Befehl benutzen dürfen solltest, wende dich an <@363354366113087491>."
        await message.channel.send(embed=e)
        return False
    else:
        return True


def get_server_actions(server_id):
    actions = []
    command_actions = {}

    server_path = dir_path + "/server_actions/" + str(server_id)
    if not os.path.exists(server_path):
        os.mkdir(server_path)
    for itm in sorted(os.listdir(server_path)):
        if itm.startswith("__"):
            continue

        spec = importlib.util.spec_from_file_location(itm, server_path + "/" + itm)
        loaded_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(loaded_module)
        actions.append(loaded_module)
        for command in loaded_module.commands:
            command_actions[command] = loaded_module
    return command_actions, actions


def parse(message: discord.Message):
    split = message.content.split(' ')
    command = split[0][1:]
    channel = message.channel
    params = split[1:]
    mentions = message.mentions
    author = message.author

    return command.lower(), channel, params, mentions, author


# TODO: Tumblr as Source
def get_gif(search_term, lmt=10, pos=None, wo_anime=False, platform=None, check_last=True):
    global last_gif
    print(f"[{Fore.MAGENTA}{'System - Gif':20}{Fore.RESET}] Get")

    if platform is None:
        if os.path.exists("cache/") and search_term in os.listdir("cache/"):
            platform = random.choice(platforms_with_local)
        else:
            platform = random.choice(platforms)

    if platform == "tenor":
        if pos is None:
            pos = random.randint(0, 100)
        if not wo_anime:
            search_term = 'anime ' + search_term

        print(f"[{Fore.MAGENTA}{'System - Gif':20}{Fore.RESET}] Using: Tenor |", search_term, lmt, pos)
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s&contentfilter=medium&pos=%s" % (search_term, tenor_key, lmt, pos))

        if r.status_code == 200:
            gifs = r.json()
            options = [itm["media"][0]['gif']["url"] for itm in gifs["results"]]
            if last_gif in options and check_last:
                options.remove(last_gif)
                print(f"[{Fore.MAGENTA}{'System - Gif':20}{Fore.RESET}]", "last_gif in options", len(options))
            sel = random.choice(options)
            last_gif = sel
            print(f"[{Fore.MAGENTA}{'System - Gif':20}{Fore.RESET}]", "Selected gif:", sel, "<-", options)
            return sel
        else:
            return None
    elif platform == "giphy":
        if pos is None:
            pos = random.randint(0, 4)
        if not wo_anime:
            search_term = 'anime ' + search_term

        print(f"[{Fore.MAGENTA}{'System - Gif':20}{Fore.RESET}] Using: Giphy |", search_term, lmt, pos)
        r = requests.get("https://api.giphy.com/v1/gifs/search?api_key=%s&q=%s&limit=%s&offset=%s&rating=PG-13" % (giphy_key, search_term, lmt, pos))

        if r.status_code == 200:
            gifs = r.json()
            options = [itm["images"]["original"]["url"] for itm in gifs["data"]]
            if last_gif in options:
                options.remove(last_gif)
                print(f"[{Fore.MAGENTA}{'System - Gif':20}{Fore.RESET}]", "last_gif in options", len(options))
            sel = random.choice(options)
            last_gif = sel
            print(f"[{Fore.MAGENTA}{'System - Gif':20}{Fore.RESET}]", "Selected gif:", sel, "<-", options)
            return sel
    elif platform == "local":
        print(f"[{Fore.MAGENTA}{'System - Gif':20}{Fore.RESET}] Using: Local |", search_term)

        options = os.listdir(f"cache/{search_term}/tenor")

        if last_gif in options:
            print(len(options))
            options.remove(last_gif)
            print(f"[{Fore.MAGENTA}{'System - Gif':20}{Fore.RESET}]", "last_gif in options", len(options))
        sel = random.choice(options)
        last_gif = sel
        print(f"[{Fore.MAGENTA}{'System - Gif':20}{Fore.RESET}]", dir_path + f"/cache/{search_term}/tenor/" + sel, "<-", f"cache/{search_term}/tenor")
        return dir_path + f"/cache/{search_term}/tenor/" + sel


def get_goat():
    goats = [g for g in os.listdir(dir_path + '/assets/goats/') if not g.endswith('.mp4') and not g.endswith('.db')]
    goat = random.choice(goats)
    print(goat, "<-", len(goats))
    return goat


def get_maxi():
    maxis = [g for g in os.listdir(dir_path + '/assets/maxitogo/') if not g.endswith('.mp4') and not g.endswith('.db')]
    maxi = random.choice(maxis)
    print(maxi, "<-", len(maxis))
    return maxi


def get_islieb(term=None):
    comics = [g for g in os.listdir(dir_path + '/assets/islieb/') if not g.endswith('.mp4') and not g.endswith('.db')]
    if term is None:
        print("Getting random comic")
        comic = random.choice(comics)
        print(comic, "<-", len(comics))
    else:
        print("Searching for comic:", term)
        term_comics = [x for x in process.extract(term, comics, limit=15) if x[1] > 75]
        if len(term_comics) > 0:
            comic = random.choice(term_comics)[0]
        else:
            print("using random")
            comic = random.choice(comics)
        print(comic, "<-", term)

    return comic
