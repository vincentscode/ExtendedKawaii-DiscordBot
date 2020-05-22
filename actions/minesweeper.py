import discord
import random
from helpers import parse

commands = ["minesweeper"]
requires_mention = False
accepts_mention = False
description = "Minesweeper! :bomb:"


async def execute(message):
    command, channel, params, mentions, author = parse(message)
    mention_strings = [m.mention for m in mentions]
    actual_params = []
    for param in params:
        if param not in mention_strings:
            actual_params.append(param)
    print("Params", params, "|", mention_strings, "=>", actual_params)
    if len(actual_params) > 0:
        try:
            columns, rows = [int(x) for x in actual_params[0].split("*")]
            print("set columns / rows", columns, rows)
            if columns < 4 or rows < 4:
                await message.channel.send('Rows / Columns must be >= 4')
                return
        except Exception:
            columns = random.randint(4, 13)
            rows = random.randint(4, 13)
    else:
        columns = random.randint(4, 13)
        rows = random.randint(4, 13)

    bombs = columns * rows - 1
    bombs = bombs / 2.5
    bombs = round(random.randint(5, round(bombs)))

    # https://github.com/DeCoded-Void/Minesweeper_discord.py
    try:
        columns = int(columns)
        rows = int(rows)
        bombs = int(bombs)
    except ValueError:
        await message.channel.send("ValueError")
        return
    if columns > 13 or rows > 13:
        await message.channel.send('The limit for the columns and rows are 13 due to discord limits...')
        return
    if columns < 1 or rows < 1 or bombs < 1:
        await message.channel.send('The provided numbers cannot be zero or negative...')
        return
    if bombs + 1 > columns * rows:
        await message.channel.send(
            ':boom:**BOOM**, you have more bombs than spaces on the grid or you attempted to make all of the spaces bombs!')
        return

    # Creates a list within a list and fills them with 0s, this is our makeshift grid
    grid = [[0 for num in range(columns)] for num in range(rows)]

    # Loops for the amount of bombs there will be
    loop_count = 0
    while loop_count < bombs:
        x = random.randint(0, columns - 1)
        y = random.randint(0, rows - 1)
        # We use B as a variable to represent a Bomb (this will be replaced with emotes later)
        if grid[y][x] == 0:
            grid[y][x] = 'B'
            loop_count = loop_count + 1
        # It will loop again if a bomb is already selected at a random point
        if grid[y][x] == 'B':
            pass

    # The while loop will go though every point though our makeshift grid
    pos_x = 0
    pos_y = 0
    while pos_x * pos_y < columns * rows and pos_y < rows:
        # We need to predefine this for later
        adj_sum = 0
        # Checks the surrounding points of our "grid"
        for (adj_y, adj_x) in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            # There will be index errors, we can just simply ignore them by using a try and exception block
            try:
                if grid[adj_y + pos_y][adj_x + pos_x] == 'B' and adj_y + pos_y > -1 and adj_x + pos_x > -1:
                    # adj_sum will go up by 1 if a surrounding point has a bomb
                    adj_sum = adj_sum + 1
            except Exception as error:
                pass
        # Since we don't want to change the Bomb variable into a number,
        # the point that the loop is in will only change if it isn't "B"
        if grid[pos_y][pos_x] != 'B':
            grid[pos_y][pos_x] = adj_sum
        # Increases the X values until it is more than the columns
        # If the while loop does not have "pos_y < rows" will index error
        if pos_x == columns - 1:
            pos_x = 0
            pos_y = pos_y + 1
        else:
            pos_x = pos_x + 1

    # Builds the string to be Discord-ready
    string_builder = []
    for the_rows in grid:
        string_builder.append(''.join(map(str, the_rows)))
    string_builder = '\n'.join(string_builder)
    # Replaces the numbers and B for the respective emotes and spoiler tags
    string_builder = string_builder.replace('0', '||:zero:||')
    string_builder = string_builder.replace('1', '||:one:||')
    string_builder = string_builder.replace('2', '||:two:||')
    string_builder = string_builder.replace('3', '||:three:||')
    string_builder = string_builder.replace('4', '||:four:||')
    string_builder = string_builder.replace('5', '||:five:||')
    string_builder = string_builder.replace('6', '||:six:||')
    string_builder = string_builder.replace('7', '||:seven:||')
    string_builder = string_builder.replace('8', '||:eight:||')
    final = string_builder.replace('B', '||:bomb:||')

    percentage = columns * rows
    percentage = bombs / percentage
    percentage = 100 * percentage
    percentage = round(percentage, 2)

    embed = discord.Embed(title=':bomb: Minesweeper :boom:')
    embed.add_field(name='Columns:', value=str(columns), inline=True)
    embed.add_field(name='Rows:', value=str(rows), inline=True)
    embed.add_field(name='Total Spaces:', value=str(columns * rows), inline=True)
    embed.add_field(name='\U0001F4A3 Count:', value=str(bombs), inline=True)
    embed.add_field(name='\U0001F4A3 Percentage:', value=f'{percentage}%', inline=True)
    embed.add_field(name='Requested by:', value=message.author.display_name, inline=True)
    embed.description = f'{final}'
    embed.set_footer(text="+minesweeper columns*rows")
    await message.channel.send(embed=embed)
