from colorama import Fore
from config import token, prefix, dev_mode
from helpers import print, parse, get_server_actions
import actions
import actions.readme
import actions.settings
import actions.propose_command
import discord
import math

if dev_mode:
    import importlib

client = discord.Client()

blocklist = ["193350207776358400"]

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
async def on_member_ban(guild, user):
    print("Guild", guild, "banned", user)


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if not message.content.startswith(prefix) or len(message.content) < 1:
        return

    command, channel, params, mentions, author = parse(message)
    if dev_mode:
        importlib.reload(actions)

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
        await get_server_actions(channel.guild.id)[0][command].execute(message)

    elif command in actions.command_actions.keys():
        print(f"[{Fore.LIGHTBLUE_EX}{message.guild.name:20}{Fore.RESET}] Executing {command} {author.name}#{author.discriminator}: \"{message.content}\"")

        if command in actions.readme.commands:
            print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Sending readme ({len(actions.actions)} actions)")
            inline = True
            if len(params) != 0:
                if params[0] == '0' or params[0] == 'short':
                    inline = True
                elif params[0] == '1' or params[0] == 'long':
                    inline = False

            embed = discord.Embed()
            embed.title = f"Liste der Befehle 1/{math.ceil(len(actions.actions) / 24)}"
            embed.description = 'Prefix: ' + prefix
            itr = 0
            page_itr = 1
            for action in actions.actions:
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
                    await channel.send(embed=embed)
                    embed = discord.Embed()
                    embed.title = f"Liste der Befehle {page_itr}/{math.ceil(len(actions.actions) / 24)}"
                    embed.description = 'Prefix: ' + prefix
                    itr = 0
            if len(embed.fields) != 0:
                print(f"Sending \"{embed.title}\"")
                await channel.send(embed=embed)

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

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='+help'))

client.run(token)
