from colorama import Fore
from config import token, prefix, dev_mode
from helpers import print
import actions
import actions.readme
import actions.settings
import discord
import math

if dev_mode:
    import importlib

client = discord.Client()


def parse(message: discord.Message):
    split = message.content.split(' ')
    command = split[0][1:]
    channel = message.channel
    params = split[1:]
    mentions = message.mentions
    author = message.author

    return command.lower(), channel, params, mentions, author


@client.event
async def on_guild_join(guild):
    print("Joined guild", guild)


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if not message.content.startswith(prefix) or len(message.content) < 1:
        return

    command, channel, params, mentions, author = parse(message)
    if dev_mode:
        importlib.reload(actions)
    if command in actions.command_actions.keys():
        print(f"[{Fore.BLUE}{message.guild.name:20}{Fore.RESET}] Executing {command} {author.name}#{author.discriminator}: \"{message.content}\")")

        if command in actions.readme.commands:
            print("Sending readme", len(actions.actions))
            inline = True
            if len(params) != 0:
                if params[0] == '1':
                    inline = False

            embed = discord.Embed()
            embed.title = f"Liste der Befehle 1/{math.ceil(len(actions.actions) / 24)}"
            embed.description = 'Prefix: ' + prefix
            itr = 0
            page_itr = 1
            for action in actions.actions:
                cmd_append = ""
                if action.requires_mention:
                    cmd_append = " [Person]"
                elif action.accepts_mention:
                    cmd_append = " [Optional: Person]"
                embed.add_field(name='**' + ' / '.join(action.commands) + cmd_append + '**', value=action.description, inline=inline)
                itr += 1
                if itr == 24:
                    page_itr += 1
                    await channel.send(embed=embed)
                    embed = discord.Embed()
                    embed.title = f"Liste der Befehle {page_itr}/{math.ceil(len(actions.actions) / 24)}"
                    embed.description = 'Prefix: ' + prefix
            if len(embed.fields) != 0:
                await channel.send(embed=embed)

        elif command in actions.settings.commands:
            print("Sending settings:", params)
            if len(params) > 0:
                pass
            else:
                embed = discord.Embed()
                embed.title = "Mögliche Einstellungen"
                embed.description = 'Prefix: ' + prefix + 'settings [Einstellung]'
                for setting_name in actions.settings.settings:
                    embed.add_field(name='**' + ' / '.join(setting_name) + '**', value=actions.settings.settings[setting_name])
                await channel.send(embed=embed)

        else:
            await actions.command_actions[command].execute(message)


@client.event
async def on_ready():
    print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Started")
    print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Name:", client.user.name)
    print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Id:", client.user.id)
    print(f"[{Fore.MAGENTA}{'System':20}{Fore.RESET}] Current guilds (max 25):", [x["name"] for x in await client.fetch_guilds().get_guilds(25)])

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='+help'))

client.run(token)
