from colorama import Fore
from config import token, prefix, dev_mode
import config
from helpers import print, parse, get_server_actions, get_server_webhooks, dir_path
import actions
import actions.readme
import actions.settings
import actions.propose_command
import discord
import math
import builtins
from datetime import datetime
import time
import asyncio
import aiohttp
import shelve
from inspect import signature

# dev mode
if dev_mode:
    import importlib

# client
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# global client
config.client = client

user_blacklist = []
server_blacklist = [435422365925507073]


# join / leave
join_leave_log = open(dir_path + "/join_leave_log.txt", "a", encoding="utf8")

# insta previews
import instaloader
iloader = instaloader.Instaloader()
# iloader.load_session_from_file(config.ig_username)

@client.event
async def on_guild_join(guild):
    print("Joined guild", guild)


@client.event
async def on_guild_update(old_guild, new_guild):
    print("Guild was updated", old_guild, "=>", new_guild)


@client.event
async def on_guild_remove(guild):
    print("Left guild", guild)

@client.event
async def on_member_join(member):
    try:
        print(f"[{Fore.LIGHTBLUE_EX}{member.guild.name:20}{Fore.RESET}]", member, "joined")
        join_leave_log.write("\t".join([str(x) for x in [time.time(), member.guild.id, "join", member.id, member.guild.member_count]]) + "\n")
        join_leave_log.flush()
    except Exception as ex:
        print("on_member_join:", ex)

@client.event
async def on_member_remove(member):
    try:
        print(f"[{Fore.LIGHTBLUE_EX}{member.guild.name:20}{Fore.RESET}]", member, "left")
        join_leave_log.write("\t".join([str(x) for x in [time.time(), member.guild.id, "leave", member.id, member.guild.member_count]]) + "\n")
        join_leave_log.flush()
    except Exception as ex:
        print("on_member_remove:", ex)

@client.event
async def on_member_ban(guild, user):
    print("Guild", guild, "banned", user)


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    server_webhooks = get_server_webhooks(message.guild.id)
    # print("server_webhooks", server_webhooks)
    wh_key = "on_message"
    if wh_key in server_webhooks:
        for wh_url in server_webhooks[wh_key]:
            try:
                print("starting req to wh", wh_url)
                async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=0.2)) as http_client:
                    req = await http_client.get(wh_url)
                    req.close()
                    print("webhook called:", wh_url)
            except Exception as ex:
                print("request to webhook failed", wh_url, ex)

    builtins.print(f"[{Fore.WHITE}" + datetime.now().strftime('%H:%M:%S.%f') + f"{Fore.RESET}] " + "[" + f"{Fore.LIGHTGREEN_EX}INFO {Fore.RESET}" + "] " + f"[{Fore.LIGHTBLUE_EX}{message.guild.name:20}{Fore.RESET}] {message.author.name}:", message.content)

    if len(message.content) < 1 and len(message.attachments) < 1:
        return

    if message.author.id in user_blacklist:
        print("Blocked user", message.author)

        title = "This user has been blacklisted."
        content = "Bot commands from this user are ignored.\nPossible reasons are misuse or suspicious activities."
        e = discord.Embed()
        e.description = content
        e.set_author(name=title)
        e.set_footer(text="Feel free to contact Vincent#0212 to learn more.")
        await message.channel.send(embed=e)
        return

    if message.guild.id in server_blacklist:
        print("Blocked guild", message.guild)

        title = "This guild has been blacklisted."
        content = "Bot commands in this guild are ignored.\nPossible reasons are misuse, suspicious activities or general concerns."
        e = discord.Embed()
        e.description = content
        e.set_author(name=title)
        e.set_footer(text="Feel free to contact Vincent#0212 to learn more.")
        await message.channel.send(embed=e)
        return

    command, channel, params, mentions, author = parse(message)
    if dev_mode:
        importlib.reload(actions)

    if not message.content.startswith(prefix):
        return

    if command in get_server_actions(channel.guild.id)[0].keys():
        print(f"[{Fore.LIGHTBLUE_EX}{message.guild.name:20}{Fore.RESET}] Executing Server Command {command} {author.name}#{author.discriminator}: \"{message.content}\"")

        class ChannelWrapper:
            def __init__(self, original):
                self.original = original

            async def send(self, content=None, *, tts=False, embed: discord.Embed=None, file=None, files=None, delete_after=None, nonce=None):
                if embed is not None:
                    embed.colour = discord.Colour.from_rgb(156, 52, 137)
                return await self.original.send(content=content, tts=tts, embed=embed, file=file, files=files, delete_after=delete_after, nonce=nonce)

        message.channel = ChannelWrapper(message.channel)
        func = get_server_actions(channel.guild.id)[0][command].execute
        if len(signature(func).parameters) == 2:
            await func(message, client)
        else:
            await func(message)

    elif command in actions.command_actions.keys():
        print(f"[{Fore.LIGHTBLUE_EX}{message.guild.name:20}{Fore.RESET}] Executing {command} {author.name}#{author.discriminator}: \"{message.content}\"")

        if command in actions.readme.commands:
            if True:
                dm_channel = await author.create_dm()

                all_relevant_actions = []
                for action in actions.actions:
                    all_relevant_actions.append(action)
                for action in get_server_actions(channel.guild.id)[0].values():
                    all_relevant_actions.append(action)

                all_relevant_actions = list(set(all_relevant_actions))

                print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Sending PRIVATE readme ({len(all_relevant_actions)} actions)")
                inline = True
                if len(params) != 0:
                    if params[0] == '0' or params[0] == 'short':
                        inline = True
                    elif params[0] == '1' or params[0] == 'long':
                        inline = False

                embed = discord.Embed()
                embed.title = f"Liste der Befehle 1/{math.ceil(len(all_relevant_actions) / 24)}"
                embed.description = 'Prefix: ' + prefix
                itr = 0
                page_itr = 1
                for action in all_relevant_actions:
                    cmd_append = ""
                    if 'readme' in action.commands:
                        cmd_append = " [Optional: Stil 0 (Default) / 1]"
                    elif action.requires_mention:
                        cmd_append = " [Person]"
                    elif action.accepts_mention:
                        cmd_append = " [Optional: Person]"
                    joined_commands = ' / '.join(action.commands)
                    joined_commands = (joined_commands[:50] + '..') if len(joined_commands) > 75 else joined_commands
                    embed.add_field(name='**' + joined_commands + cmd_append + '**', value=action.description, inline=inline)
                    itr += 1
                    if itr == 24:
                        page_itr += 1
                        print(f"Sending \"{embed.title}\"")
                        await dm_channel.send(embed=embed)
                        embed = discord.Embed()
                        embed.title = f"Liste der Befehle {page_itr}/{math.ceil(len(all_relevant_actions) / 24)}"
                        embed.description = 'Prefix: ' + prefix
                        itr = 0

                if len(embed.fields) != 0:
                    print(f"Sending \"{embed.title}\"")
                    await dm_channel.send(embed=embed)
                
                await channel.send("Ich habe dir die Hilfe via PM gesendet. Es sind X Seiten, dauert also nen Moment. owo")

        elif command in actions.settings.commands:
            print("Sending settings:", params)
            if len(params) > 0:
                pass
            else:
                await channel.send("Coming soon™")
                # embed = discord.Embed()
                # embed.title = "Mögliche Einstellungen"
                # embed.description = 'Prefix: ' + prefix + 'settings [Einstellung]'
                # for setting_name in actions.settings.settings:
                #     embed.add_field(name='**' + ' / '.join(setting_name) + '**', value=actions.settings.settings[setting_name])
                # await channel.send(embed=embed)
        elif command in actions.propose_command.commands:
            class ChannelWrapper:
                def __init__(self, original):
                    self.original = original

                async def send(self, content=None, *, tts=False, embed: discord.Embed=None, file=None, files=None, delete_after=None, nonce=None):
                    if embed is not None:
                        embed.colour = discord.Colour.from_rgb(156, 52, 137)
                    return await self.original.send(content=content, tts=tts, embed=embed, file=file, files=files, delete_after=delete_after, nonce=nonce)

            message.channel = ChannelWrapper(message.channel)
            await actions.command_actions[command].execute(message, client)


        else:
            class ChannelWrapper:
                def __init__(self, original):
                    self.original = original

                async def send(self, content=None, *, tts=False, embed: discord.Embed=None, file=None, files=None, delete_after=None, nonce=None):
                    if embed is not None:
                        embed.colour = discord.Colour.from_rgb(156, 52, 137)
                    return await self.original.send(content=content, tts=tts, embed=embed, file=file, files=files, delete_after=delete_after, nonce=nonce)

            message.channel = ChannelWrapper(message.channel)
            await actions.command_actions[command].execute(message)


@client.event
async def on_ready():
    print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Started")
    print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Name:", client.user.name)
    print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Id:", client.user.id)
    print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Current guilds (max 25):", [x["name"] for x in await client.fetch_guilds().get_guilds(25)])

    asyncio.create_task(change_rainbow_role_every_nh())

    # await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='+help'))

async def change_rainbow_role():
    global client

    rainbow_servers = [923241820073386024]
    rainbow_role_name = "✨ 🌈"

    print("ROLE COLOR CHANGE")
    for rainbow_server_id in rainbow_servers:
        guild = client.get_guild(rainbow_server_id)
        for role in guild.roles:
            if role.name == rainbow_role_name:
                await role.edit(colour=discord.Colour.random())
                break

async def change_rainbow_role_lena():
    global client

    rainbow_servers = [923241820073386024]
    rainbow_role_name = "✨ 🌈 Hibbelblob"

    print("ROLE COLOR CHANGE LENA")
    for rainbow_server_id in rainbow_servers:
        guild = client.get_guild(rainbow_server_id)
        for role in guild.roles:
            if role.name == rainbow_role_name:
                await role.edit(colour=discord.Colour.random())
                break



# rainbow role
async def change_rainbow_role_every_nh():
    while True:
        # rainbow role
        await change_rainbow_role()

        # sleep 30m
        await asyncio.sleep(60 * 30)

        # lena role        
        await change_rainbow_role_lena()

        # sleep 30m
        await asyncio.sleep(60 * 30)

config.change_rainbow_role = change_rainbow_role
config.change_rainbow_role_lena = change_rainbow_role_lena
client.run(token)
