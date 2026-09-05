import discord
import matplotlib.pyplot as plt
import numpy as np
import asyncio
from matplotlib.dates import date2num
from matplotlib.ticker import MaxNLocator
from helpers import dir_path, parse, print
import requests
from datetime import datetime, date, time, timedelta
import time as t
import data.config as config
import statsmodels.api as sm


DISCORD_EPOCH = 1420070400000
def snowflake2date(snowflake):
    ts = (snowflake / 4194304 + DISCORD_EPOCH) / 1000 # 1000x windows conversion
    return datetime.fromtimestamp(int(ts))

def date2snowflake(date):
    ts = datetime.combine(date, time()).timestamp()
    snowflake = (ts * 1000 - DISCORD_EPOCH) * 4194304
    return int(snowflake)

commands = ["howmanymsg"]
requires_mention = False
accepts_mention = False
description = "howmany msgs?! :O"


s = requests.Session()
s.headers.update(config.discord_headers)

async def get_messages_between_dates(min_date, max_date, guild_id):
    global s
    params = (
        ('min_id', date2snowflake(min_date)),
        ('max_id', date2snowflake(max_date)),
        ('limit', 1),
    )

    r = s.get(f'https://discord.com/api/v9/guilds/{guild_id}/messages/search', params=params)
    j = r.json()
    if r.status_code != 200:
        raise Exception(f"API Response Code was: {r.status_code}")
    if 'total_results' not in j:
        raise Exception(f"Key total_results not in {list(j.keys())}")
    return j['total_results']

min_wait_time = 30

async def execute(message):
    global last_use_time, min_wait_time
    try:
        # parse message
        command, channel, params, mentions, author = parse(message)
        guild_id = message.guild.id

        # parse message options
        vapi_mode = False
        dump_mode = False
        if len(params) > 0:
            if "vapimode" in params:
                vapi_mode = True
            if "dump" in params:
                dump_mode = True

        # rate limiting
        if not hasattr(config, "last_use_time"):
            config.last_use_time = 0

        admin_id = 363354366113087491
        if t.time() - config.last_use_time < min_wait_time and message.author.id != admin_id:
            await message.channel.send(f"Bitte noch {round(min_wait_time - (t.time() - config.last_use_time))}s warten!")
            return

        config.last_use_time = t.time()

        # load cache
        cache_path = f"{dir_path}/data/messages_per_day_cache/{guild_id}.tsv"
        with open(cache_path, "r", encoding="utf8") as f:
            lines = [x.split("\t") for x in f.read().split("\n") if x != ""]
            dates = []
            values = []
            for l in lines:
                date_parts = [int(x) for x in l[0].split("-")]
                date_value = date(date_parts[0], date_parts[1], date_parts[2])
                value = int(l[1])

                dates.append(date_value)
                values.append(value)

        # get new data
        start_date = dates[0]
        end_date = datetime.today().date()
        with open(dir_path + f"/data/messages_per_day_cache/{guild_id}.tsv", "a", encoding="utf8") as f:
            cur_date = dates[-1] + timedelta(days=1)
            wait = False
            while cur_date <= end_date:
                if wait:
                    await asyncio.sleep(8)
                else:
                    wait = True

                mc = await get_messages_between_dates(cur_date, cur_date + timedelta(days=1), guild_id)

                dates.append(cur_date)
                values.append(mc)
                
                # add to cache if not today
                if cur_date != end_date:
                    f.write(f"{cur_date}\t{mc}\n")
                    await message.channel.send(f"New Data Point: {guild_id} | {cur_date} => {mc}")
                
                cur_date += timedelta(days=1)

        # plot setup
        plt.clf()
        plt.ylabel('# msgs', color="b")
        plt.tick_params(axis='y', labelcolor="b")
        fig, ax = plt.subplots()
        ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        fig.autofmt_xdate()

        # extract data
        x = [date2num(x) for x in dates][:-1] # dates
        x_d = []
        for x_val in x[:-1]:
            for i in range(0, 10):
                x_d.append(x_val + i / 10)
        x_d.append(x[-1])
        y = values[:-1]

        # plot data
        if vapi_mode:
            results = sm.OLS(y, sm.add_constant(x)).fit()
            results2 = sm.RLM(y, sm.add_constant(x), M=sm.robust.norms.HuberT()).fit()
            results3 = sm.GLM(y, sm.add_constant(x), family=sm.families.Gamma()).fit()

            await message.channel.send("```" + str(results.summary()) + "```")
            await message.channel.send("```" + str(results2.summary()) + "```")
            await message.channel.send("```" + str(results3.summary()) + "```")

            plt.plot(x, y, "o", label="Data")
            plt.plot(x, results.fittedvalues, "r--.", label="OLS")
            plt.plot(x, results2.fittedvalues, "b--", label="RLM")
            plt.plot(x, results3.fittedvalues, "g--", label="GLM")
            plt.scatter([dates[-1]], [values[-1]], color="gray", label="Today (TBD)")

        else:
            plt.plot(dates, values, color="b", label="Message Count")
            # plt.scatter(dates, values, color="b", label="Data")
            # plt.scatter([dates[-1]], [values[-1]], color="gray", label="Today (TBD)")

            p1 = np.poly1d(np.polyfit(x, y, 1))
            p3 = np.poly1d(np.polyfit(x, y, 3))
            plt.plot(x_d, p1(x_d), 'r--', label="Polyfit 1st degree")
            plt.plot(x_d, p3(x_d), 'y--', label="Polyfit 3rd degree")

        # plot setup
        legend = ax.legend(loc="best")
        plt.rcParams['axes.facecolor'] = 'white'
        plt.rcParams['axes.edgecolor'] = 'white'
        plt.rcParams['axes.grid'] = True
        plt.rcParams['grid.alpha'] = 1
        plt.rcParams['grid.color'] = "#cccccc"
        plt.rcParams['axes.axisbelow'] = True
        plt.grid(True)
        plt.ylim(ymin=0, ymax=None)
        ax.set_axisbelow(True)

        # show / save
        fig_path = dir_path + f"/{guild_id}_msgs_graph.png"
        plt.savefig(fig_path)

        if dump_mode:
            file = discord.File(cache_path, filename="message_count.tsv")
            await message.channel.send(file=file)
        else:
            s1 = "Data Start: " + str(start_date) + "\nData End: " + str(end_date) + "\n"
            s2 = "Total Messages: " + str(sum(values))

            embed = discord.Embed()
            embed.title = f"Message Count History"
            embed.description = s1 + "\n" + s2
            embed.set_image(url="attachment://" + "graph.png")
            embed.set_footer(text="Die Zahlen sagen was die Zahlen sagen!")
            file = discord.File(fig_path, filename="graph.png")
            await message.channel.send(file=file, embed=embed)
    except Exception as ex:
        print(str(ex))
        await message.channel.send("I failed :(")
        await message.channel.send(str(ex))
