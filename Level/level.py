import asyncio
import discord
import random
import requests
import datetime
import openpyxl
import sys
import urllib.request
from bs4 import BeautifulSoup
from discord.ext import commands
from sympy import expand, factor, Symbol
from discord.utils import get
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='^^', help_command=None, intents=intents)

@bot.event
async def on_ready():
    print('다음 봇으로 연결됨:')
    print(bot.user.name)
    print(bot.user.id)
    print('벨코즈버프좀')

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    amour = message.author.id
    requirement = [210, 315, 476, 707, 1064, 1596, 2394, 3591, 5383, 8071]
    while True:
        if(os.path.isfile("/Level/level/" + str(amour) + ".txt")):
            f = open("/Level/exp/" + str(amour) + ".txt", "r")
            exp = f.read()
            f.close()
            expp = int(exp)
            exppp = expp + 1
            f = open("/Level/exp/" + str(amour) + ".txt", "w")
            f.write(str(exppp))
            f.close()
            g = open("/Level/requirement/" + str(amour) + ".txt", "r")
            req = g.read()
            g.close()
            h = open("/Level/level/" + str(amour) + ".txt", "r")
            lvl = h.read()
            h.close()
            if exppp == int(req):
                lvlup = int(lvl) + 1
                h = open("/Level/level/" + str(amour) + ".txt", "w")
                h.write(str(lvlup))
                h.close()
                requp = requirement[int(lvl)]
                g = open("/Level/requirement/" + str(amour) + ".txt", "w")
                g.write(str(requp))
                g.close()
                embed = discord.Embed(color=0xff6060, timestamp = message.created_at)
                embed.set_author(name="Level Up!"),
                embed.set_thumbnail(url=message.author.avatar),
                embed.set_footer(text=f'{message.author}', icon_url=message.author.avatar)
                embed.add_field(name="레벨", value=str(lvlup),inline=False)
                embed.add_field(name="EXP", value=str(exppp)+"/"+str(requp), inline=False)
                await message.channel.send(embed=embed) 
        break

bot.run("YOUR TOKEN")