import discord

commands = ["uwu", "owo", "UwU", "OwO"]
requires_mention = False
accepts_mention = True
description = "uwu"

uwu_dictionary = {
    ' to ': ' 2 ',
    ' you ': ' u ',
    ' hate ': ' h8 ',
    ' this ': ' dis ',
    '\'re': '\'w',
    'ck': 'c',
    'oo': 'OwO',
    ' th': ' de',
    'qu': 'q',
    'r': 'w',
    'l': 'w',
    'ww': 'w'
}


async def execute(message: discord.Message):
    """
    this command turns ordinary text messages to uwu text
    i.g. 'i want to shoot myself' -> 'i want 2 shOwOt mysewf'

    to do:
      -some words have alternate meanings once they have been passed trough this translator:
       i.g. 'i hate my life' -> 'i h8 my wife'
       for now this is a feature
    """
    
    text = message.content[len("+uwu"):].strip(" ")

    for rule in uwu_dictionary.items():
        text = text.replace(rule[0], rule[1])

    await message.channel.send('```%s```' % text)
