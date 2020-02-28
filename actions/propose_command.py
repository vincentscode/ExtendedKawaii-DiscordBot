import asyncio
import os
import random
import re

from helpers import print
import discord
import main
import helpers

commands = ["cmdvorschlag", "addcmd", "propcmd", "proposecommand", "+cmd"]
requires_mention = False
accepts_mention = False
description = "Propose a command for me :O"


class MenuStep:
    def __init__(self, title_text, description_text, footer_text, footer_icon, on_next_command, wait_for_response=True):
        self.embed = discord.Embed()
        self.embed.title = title_text
        self.embed.description = description_text
        self.embed.set_footer(text=footer_text, icon_url=footer_icon)

        self.on_next_command = on_next_command

        self.wait_for_response = wait_for_response

    async def send(self, channel: discord.TextChannel):
        await channel.send(embed=self.embed)

    def on_next(self, msg):
        return self.on_next_command(msg)


async def execute(message):
    proposed_cmd = {}

    def get_status():
        return f"Status: ```" \
               f"\nName / Befehl:                  {proposed_cmd.get('proposed_command_name', 'None')}" \
               f"\nAlternative Befehle / Aliases:  {', '.join(proposed_cmd.get('proposed_command_aliases', [])) if proposed_cmd.get('proposed_command_aliases', []) != [] and proposed_cmd.get('proposed_command_aliases', []) is not None else 'None'}" \
               f"\n" \
               f"\nAntwort Gif:                    {proposed_cmd.get('proposed_command_gif', 'None')}" \
               f"\nAntwort Text (ohne Ping):       {proposed_cmd.get('response_description', 'None') if proposed_cmd.get('response_description', 'None') is not None else 'None'}" \
               f"\nAntwort Text (mit Ping):        {proposed_cmd.get('response_description_ping', 'None') if proposed_cmd.get('response_description_ping', 'None') is not None else 'None'}" \
               f"\n" \
               f"\nAuthor:                         {proposed_cmd.get('proposed_command_author')}" \
               f"\n```"

    def step_name(msg: discord.Message):
        proposed_cmd['proposed_command_name'] = msg.content
        proposed_cmd['proposed_command_author'] = msg.author.name + "#" + msg.author.discriminator
        proposed_cmd['proposed_command_author_icon'] = msg.author.avatar_url
        return 1

    def step_aliases(msg):
        proposed_cmd['proposed_command_aliases'] = ([x.replace(" ", "") for x in msg.content.split(",")] if msg.content != 'None' else None)
        return 1

    def step_gif(msg):
        proposed_cmd['proposed_command_gif'] = msg.content
        return 1

    def step_description_no_ping(msg):
        proposed_cmd['response_description'] = (msg.content if msg.content != 'None' else None)
        return 1

    def step_description_ping(msg):
        proposed_cmd['response_description_ping'] = (msg.content if msg.content != 'None' else None)
        return 1

    def step_request_command(msg):
        print("Requested Command:", proposed_cmd)

        dir_path = helpers.dir_path + "/proposed_commands"
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        command_template = f'''
import discord
from helpers import get_gif

commands = ["{proposed_cmd['proposed_command_name']}"{", " + ', '.join(["'" + x + "'" for x in proposed_cmd['proposed_command_aliases']]) if proposed_cmd['proposed_command_aliases'] is not None and len(proposed_cmd['proposed_command_aliases']) != 0 else ""}]
requires_mention = False
accepts_mention = {'{Pings}' in proposed_cmd['response_description_ping']}
description = "{proposed_cmd['proposed_command_name']} by {proposed_cmd['proposed_command_author']}"


async def execute(message):
    gif = get_gif("{proposed_cmd['proposed_command_gif']}", lmt=25, pos=0, wo_anime=True)

    embed = discord.Embed()
    if accepts_mention:
        if len(message.mentions) == 1:
            # 1 mention
            embed.description = f"{proposed_cmd['response_description_ping'].replace('{Pings}', '{message.mentions[0].mention}').replace('{Author}', '{message.author.mention}')}"
        elif len(message.mentions) > 1:
            # > 1 mentions
            embed.description = f"{proposed_cmd['response_description_ping'].replace('{Pings}', '{', '.join([x.mention for x in message.mentions]}').replace('{Author}', '{message.author.mention}')}"
        else:
            # 0 mentions
            embed.description = "{proposed_cmd['response_description'].replace('{Author}', '{message.author.mention}')}"
    else:
        embed.description = "{proposed_cmd['response_description'].replace('{Author}', '{message.author.mention}')}"
    
    embed.set_footer(text="Ein Befehl von {proposed_cmd['proposed_command_author']}", icon_url="{proposed_cmd['proposed_command_author_icon']}")
    embed.set_image(url=gif)
    await message.channel.send(embed=embed)
'''
        f = open(dir_path + "/" + re.sub(r'[\\/*?:"<>|]', '', proposed_cmd['proposed_command_author'] + proposed_cmd['proposed_command_name'] + str(random.randint(0, 2000))) + ".py", "w", encoding="utf8")
        f.write(command_template)
        f.flush()
        f.close()
        return 1

    menu_steps = [
        lambda: MenuStep(
            "Befehl erstellen",
            "Erstelle deinen eigenen kleinen Befehl für den Bot!\n(Für komplexere Befehle ping mich einfach :D)\n\nSende den **Namen** deines Befehls um fortzufahren\nSende **Cancel** um das Menü zu verlassen",
            'Ein Bot von Vincent#0212', 'https://avatars0.githubusercontent.com/u/26576880?s=60&v=4',
            step_name
         ),

        lambda: MenuStep(
            "Befehl erstellen",
            get_status() +
            f"\n"
            f"\nSende **Alternative Befehle / Aliases (durch Kommata getrennt)** deines Befehls um fortzufahren"
            f"\nSende **None** um keine Alternativen Befehle zu registrieren"
            f"\nSende **Cancel** um das Menü zu verlassen und den Befehl zu verwerfen",
            'Ein Bot von Vincent#0212', 'https://avatars0.githubusercontent.com/u/26576880?s=60&v=4',
            step_aliases
        ),

        lambda: MenuStep(
            "Befehl erstellen",
            get_status() +
            f"\n"
            f"\nSende den **Suchterm für das Gif** deines Befehls um fortzufahren"
            f"\nSende **Cancel** um das Menü zu verlassen und den Befehl zu verwerfen",
            'Ein Bot von Vincent#0212', 'https://avatars0.githubusercontent.com/u/26576880?s=60&v=4',
            step_gif
        ),

        lambda: MenuStep(
            "Befehl erstellen",
            get_status() +
            f"\n"
            f"\nSende den **Text für die Antwort wenn *keine* Nutzer gepingt werden** deines Befehlsum fortzufahren"
            f"\nVerwende um den Author einzubinden {{Author}}"
            f"\nSende **None** um keinen Text anzugeben"
            f"\nSende **Cancel** um das Menü zu verlassen und den Befehl zu verwerfen",
            'Ein Bot von Vincent#0212', 'https://avatars0.githubusercontent.com/u/26576880?s=60&v=4',
            step_description_no_ping
        ),

        lambda: MenuStep(
            "Befehl erstellen",
            get_status() +
            f"\n"
            f"\nSende den **Text für die Antwort wenn Nutzer gepingt werden** deines Befehlsum fortzufahren"
            f"\nVerwende um den Author einzubinden {{Author}} und den/die gepingten Nutzer einzubinden {{Pings}}"
            f"\nSende **None** um keinen Text anzugeben"
            f"\nSende **Cancel** um das Menü zu verlassen und den Befehl zu verwerfen",
            'Ein Bot von Vincent#0212', 'https://avatars0.githubusercontent.com/u/26576880?s=60&v=4',
            step_description_ping
        ),

        lambda: MenuStep(
            "Befehl erstellen",
            get_status() +
            f"\n"
            f"\nBitte Bestätige den Befehl mit **Ok**"
            f"\nSende **Cancel** um das Menü zu verlassen und den Befehl zu verwerfen",
            'Ein Bot von Vincent#0212', 'https://avatars0.githubusercontent.com/u/26576880?s=60&v=4',
            step_request_command
        ),

        lambda: MenuStep(
            "Befehl erstellen",
            get_status() +
            f"\n"
            f"\nBefehl wird angefragt - bitte habe etwas Geduld.",
            'Ein Bot von Vincent#0212', 'https://avatars0.githubusercontent.com/u/26576880?s=60&v=4',
            lambda: None, wait_for_response=False
        )
    ]

    t_out = 60.0

    menu_idx = 0

    while True:
        print("Sending Menu item", menu_idx)
        current_step = menu_steps[menu_idx]()
        await current_step.send(message.channel)

        if not current_step.wait_for_response:
            return

        def response_check(msg):
            return msg.channel == message.channel.original and msg.author.mention == message.author.mention

        try:
            response_msg = await main.client.wait_for('message', timeout=t_out, check=response_check)
            print("Waiting for Response (Timeout: " + str(t_out) + ")")
        except asyncio.TimeoutError:
            print("No Response (Timeout)")
            await message.channel.send("Keine Antwort - Cancelled.")
        else:
            print("Response: " + response_msg.content)
            if response_msg.content.lower() == 'cancel':
                await message.channel.send("Cancelled.")
                print("Cancelled")
                return

            resp = current_step.on_next(response_msg)
            if resp == 'Cancel':
                print("Ended")
                return

            menu_idx += resp

