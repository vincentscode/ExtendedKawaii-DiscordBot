from colorama import Fore
from data.config import token, prefix, dev_mode
import data.config as config
from helpers import print, parse
import actions
import actions.readme
import discord
import math
import builtins
from datetime import datetime
import asyncio

# dev mode
if dev_mode:
    import importlib

# client
intents = discord.Intents.all()
client = discord.Client(intents=intents)

# global client
config.client = client

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
    print(f"[{Fore.LIGHTBLUE_EX}{member.guild.name:20}{Fore.RESET}]", member, "joined")

@client.event
async def on_member_remove(member):
    print(f"[{Fore.LIGHTBLUE_EX}{member.guild.name:20}{Fore.RESET}]", member, "left")

@client.event
async def on_member_ban(guild, user):
    print("Guild", guild, "banned", user)

class MyChannelWrapper:
    def __init__(self, original):
        self.original = original

    async def send(self, content=None, *, tts=False, embed: discord.Embed | None = None, file=None, files=None, delete_after=None, nonce=None):
        if embed is not None:
            embed.colour = discord.Colour.from_rgb(156, 52, 137)
        return await self.original.send(content=content, tts=tts, embed=embed, file=file, files=files, delete_after=delete_after, nonce=nonce)

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    
    if not message.guild:
        return

    builtins.print(f"[{Fore.WHITE}" + datetime.now().strftime('%H:%M:%S.%f') + f"{Fore.RESET}] " + "[" + f"{Fore.LIGHTGREEN_EX}INFO {Fore.RESET}" + "] " + f"[{Fore.LIGHTBLUE_EX}{message.guild.name:20}{Fore.RESET}] {message.author.name}:", message.content)

    if len(message.content) < 1 and len(message.attachments) < 1:
        return

    command, channel, params, _, author = parse(message)
    assert channel.guild
    if dev_mode:
        importlib.reload(actions)

    if not message.content.startswith(prefix):
        return
    elif command in actions.command_actions.keys():
        print(f"[{Fore.LIGHTBLUE_EX}{message.guild.name:20}{Fore.RESET}] Executing {command} {author.name}#{author.discriminator}: \"{message.content}\"")

        if command in actions.readme.commands:
            if True:
                dm_channel = await author.create_dm()

                all_relevant_actions = []
                for action in actions.actions:
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
        else:
            message.channel = MyChannelWrapper(message.channel) # type: ignore
            await actions.command_actions[command].execute(message)
    else:
        print("not a command:", message.content)
        print("valid commands:", actions.command_actions.keys())

is_initial_on_ready = True

@client.event
async def on_ready():
    global is_initial_on_ready

    assert client.user

    print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Started")
    print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Name:", client.user.name)
    print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Id:", client.user.id)
    print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Current guilds (max 200):", [x.name async for x in client.fetch_guilds()])

    if is_initial_on_ready:
        asyncio.create_task(change_rainbow_role_every_nh())
        is_initial_on_ready = False

async def change_rainbow_role():
    global client

    rainbow_servers = [923241820073386024]
    rainbow_role_name = "✨ 🌈"

    print("ROLE COLOR CHANGE")
    for rainbow_server_id in rainbow_servers:
        guild = client.get_guild(rainbow_server_id)
        assert guild

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
        assert guild

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
