from config import token, prefix, dev_mode
from helpers import print
import actions
import actions.readme

import discord

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
async def on_message(message):
    if message.author == client.user:
        return

    if not message.content.startswith(prefix) or len(message.content) < 1:
        return

    command, channel, params, mentions, author = parse(message)
    if dev_mode:
        importlib.reload(actions)
    if command in actions.command_actions.keys():
        print("Executing", command, "({}#{}: \"{}\")".format(author.name, author.discriminator, message.content))

        if command in actions.readme.commands:
            print("Sending readme")
            inline = True
            if len(params) != 0:
                if params[0] == '1':
                    inline = False

            embed = discord.Embed()
            embed.title = "Liste der Befehle"
            embed.description = 'Prefix: ``' + prefix + '``'
            for action in actions.actions:
                cmd_append = ""
                if action.requires_mention:
                    cmd_append = " [Person]"
                elif action.accepts_mention:
                    cmd_append = " [Optional: Person]"
                embed.add_field(name='**' + ' / '.join(action.commands) + cmd_append + '**', value=action.description, inline=inline)
            await channel.send(embed=embed)
        else:
            await actions.command_actions[command].execute(message)


@client.event
async def on_ready():
    print('Started')
    print('Name:', client.user.name)
    print('Id:', client.user.id)
    print('Current guilds (max 25):', [x["name"] for x in await client.fetch_guilds().get_guilds(25)])

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='+help'))

client.run(token)
