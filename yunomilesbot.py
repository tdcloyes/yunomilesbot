import discord
import logging
import datetime
from discord import Intents
from discord.ext import commands, tasks
import genius_scraper
import json
from config import *

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print('{:%H:%M:%S}: boutta drop bars'.format(datetime.datetime.now()))


@bot.command()
async def random(ctx):
    f = open('Lyrics_YunoMiles.json')
    data = json.load(f)
    bar, title, year = genius_scraper.random_song_bar(data)
    await ctx.send(f'> {bar}\n- *{title}* ({year})')
    f.close()


@bot.command()
async def bar(ctx, *, user_input):
    f = open('Lyrics_YunoMiles.json')
    data = json.load(f)
    bar, title, year = genius_scraper.chosen_song_bar(data, user_input)
    await ctx.send(f'> {bar}\n- *{title}* ({year})')
    f.close()


bot.run(bot_api_key)
