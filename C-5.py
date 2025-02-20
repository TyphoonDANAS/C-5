# Work with Python 3.8
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
game = discord.Game("^^도움말을 입력해주세요.")
bot = commands.Bot(command_prefix='^^', activity=game, help_command=None, intents=intents)

@bot.event
async def on_ready():
    print('다음 봇으로 연결됨:')
    print(bot.user.name)
    print(bot.user.id)
    print('벨코즈버프좀')
    serverlist = []
    memberlist = []
    for guild in bot.guilds:
        serverlist.append("**" + str(guild.name) + "**`(" + str(guild.id) + ")`")
        for i in guild.members:
            if i not in memberlist:
                memberlist.append(i)
    while True:
        await bot.change_presence(activity=discord.Game("^^도움말을 입력해주세요."))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(str(len(serverlist)) + "개의 서버"))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(str(len(memberlist)) + "명의 사용자"))
        await asyncio.sleep(5)
    

@bot.command(pass_context = True)
async def 주사위(ctx):
    randomNum = random.randrange(1, 7)
    if randomNum == 1:
        consequence = discord.Embed(description = ':game_die: ' + ':one:', color = (0xFF6060))
        await ctx.send(embed = consequence)
    if randomNum == 2:
        consequence = discord.Embed(description = ':game_die: ' + ':two:', color = (0xFF6060))
        await ctx.send(embed = consequence)
    if randomNum == 3:
        consequence = discord.Embed(description = ':game_die: ' + ':three:', color = (0xFF6060))
        await ctx.send(embed = consequence)
    if randomNum == 4:
        consequence = discord.Embed(description = ':game_die: ' + ':four:', color = (0xFF6060))
        await ctx.send(embed = consequence)
    if randomNum == 5:
        consequence = discord.Embed(description = ':game_die: ' + ':five:', color = (0xFF6060))
        await ctx.send(embed = consequence)
    if randomNum == 6:
        consequence = discord.Embed(description = ':game_die: ' + ':six:', color = (0xFF6060))
        await ctx.send(embed = consequence)

@bot.command("도움")        
async def 도움(ctx, arg):
    if arg == "기타":
        consequence = discord.Embed(title = 'C-5 기타 도움말', description = '**^^주사위**: C-5가 주사위를 던집니다.' + 
                                    '\n**^^멈뭄미/엉엉이**: 모든 ㅇ/ㅁ을 ㅁ/ㅇ으로 바꿉니다.' + 
                                    '\n**^^앵무새**: 말을 따라합니다.' + 
                                    '\n**^^병든앵무새**: 말을 이상하게 따라합니다.' +
                                    '\n**^^동전뒤집기**: 동전 뒤집기 게임을 시작합니다.', color = (0xFF6060))
        await ctx.author.send(embed = consequence)
    if arg == "기본":
        consequence = discord.Embed(title = 'C-5 기본 도움말', description = '**^^핑**: 핑을 알려줍니다.(ms)\n**^^계산**: 식을 계산합니다. 사용 방법은 `^^도움 계산`을 입력하세요.', color = (0xFF6060))
        await ctx.author.send(embed = consequence)

    if arg == "계산":
        consequence = discord.Embed(title = 'C-5 계산 도움말', description = '1. 지수는 ^로 표기하세요.(예: 2^3)\n2. 루트(제곱근)은 sqrt(n)으로 표기하세요.(예: sqrt(144))\n3. 변수가 숫자가 아닐 때에는 x나 y를 사용해야 합니다.\n4. 로그(log)는 log(n)으로 표기하세요.(예: log(100))\n5. 오일러 상수(자연로그의 밑)은 e로 표기하세요.(예: 5e)\n6. 기타: π는 pi로(예: 2*pi) 표기하세요.(ln은 지원하지 않습니다)', color = (0xFF6060))
        await ctx.author.send(embed = consequence)

@bot.command("도움말")
async def 도움말(ctx):
    consequence = discord.Embed(title = 'C-5 도움말', description = '**^^도움 기본**: 기본 도움말을 표시합니다.\n**^^도움 관리**: 관리 도움말을 표시합니다.\n**^^도움 기타**: 기타 도움말을 표시합니다.', color = (0xFF6060))
    await ctx.author.send(embed = consequence)

@bot.command("버전")
async def 버전(ctx):
    consequence = discord.Embed(title = 'C-5 버전: 3.0.3', description = 'Typhoon Code: Kalmaegi', color = (0xFF6060))
    await ctx.send(embed = consequence)

@bot.command("정보")
async def 정보(ctx,user:discord.Member=None):
    embed = discord.Embed(color=0xff6060, timestamp = ctx.message.created_at)

    embed.set_author(name=f"C-5 사용자 정보 - {user}"),
    embed.set_thumbnail(url=user.avatar),
    embed.set_footer(text=f'{ctx.author}이 요청함', icon_url=ctx.author.avatar)

    embed.add_field(name="ID", value=user.id,inline=False)
    embed.add_field(name="닉네임", value=user.display_name, inline=False)
    embed.add_field(name="계정 생성", value=user.created_at, inline=False)
    embed.add_field(name="서버 참가", value=user.joined_at, inline=False)
    embed.add_field(name="봇 여부", value=user.bot, inline=False)
    await ctx.send(embed=embed)

@bot.command("서버")
async def 서버(ctx):
    embed = discord.Embed(title="C-5 서버 정보", color=0xff6060, timestamp = ctx.message.created_at)
    embed.set_thumbnail(url=ctx.guild.icon),
    embed.set_footer(text=f'{ctx.author}이 요청함', icon_url=ctx.author.avatar)
    embed.add_field(name="서버 이름", value=ctx.message.guild.name, inline=False)
    embed.add_field(name="인원 수", value=len(ctx.message.guild.members), inline=False)
    embed.add_field(name="채널 수", value=len(ctx.message.guild.channels), inline=False)
    embed.add_field(name="보안 단계", value=f"{ctx.guild.verification_level}", inline=False)
    embed.add_field(name="역할 수", value=len(ctx.guild.roles), inline=False)
    await ctx.send(embed=embed)
    
@bot.command("삭제")
async def 삭제(ctx, amount : int):
    msg = amount + 1
    await ctx.channel.purge(limit = msg)
    await ctx.send(str(amount) + "개의 메시지가 삭제되었습니다.")
    await asyncio.sleep(2)
    await ctx.channel.purge(limit = 1)

@bot.command("인수분해")
async def 인수분해(ctx, a, b, c):
    try:
        x = Symbol('x')
        aint = int(a)
        bint = int(b)
        cint = int(c)
        bunhae = factor(aint * x**2 + bint * x + cint)
        await ctx.send(bunhae)
    except Exception as WASANS:
            await ctx.send("오류가 발생했습니다.\n`" + str(WASANS) + "`")

@bot.command("뒷메")
async def 뒷메(ctx):
    user_id_list = []
    for user_id in user_id_list:
        user = bot.get_user(user_id)
        for i in range(10):
            if ctx.author.id == 416226495640502273:
                await user.send('Send Message')
            else:
                return
    
    
@bot.command("배워")
async def 배워(ctx, *, arg):
    text = arg
    st = text.split(' ')
    wd = st[0]
    del st[0]
    pmn = st
    mn = " ".join(pmn)
    if(os.path.isfile("/Bot_Dictionary/" + wd + ".txt")):
            await ctx.send("이미 배운 단어입니다.")
            return
    else:
        f = open("/Bot_Dictionary/" + wd + ".txt", "w")
        f.write(mn + "\n```" + str(ctx.author) + " 님이 알려주셨어요!```")
        f.close()
        await ctx.send("단어 " + wd + "을(를) 배웠습니다.")
        return

@bot.command("단어")
async def 단어(ctx, *, arg):
    try:
        text = arg
        if(os.path.isfile("/Bot_Dictionary/" + text + ".txt")):
            f = open("/Bot_Dictionary/" + text + ".txt", "r")
            daneo = f.read()
            f.close()
            await ctx.send(daneo)
            return
        else:
            await ctx.send("그게 뭔지 잘 모르겠어요...")
            return
    except Exception as WASANS:
        await ctx.send("오류가 발생했습니다.\n`" + str(WASANS) + "`")
    
@bot.command("핑")
async def 핑(ctx):
    await ctx.send(f'퐁! {round(bot.latency * 1000)} ms')

@bot.command("먹어")
async def 먹어(ctx, *, arg):
    reac = ['*냠냠*', ctx.author.mention + '님, 이걸 먹으라고 주셨어요??', '*(쿰척쿰척)*', '어...갑자기 배불러요 :grinning:', '저기...혹시 드셔보신 건가요?', '**카악 퉷**', '저 급한 약속이 생겼어요! 못 먹어서 죄송해요 ㅎㅎ']
    csq = random.choice(reac)
    await ctx.send("음식:`" + str(arg) + "`\n" + str(csq))

@bot.command("공지")
async def 공지(ctx, *, arg):
    if ctx.author.id == 416226495640502273:
        channellist = []
        amount = 0
        for i in range(len(channellist)):
            amount = amount + 1
            channel = bot.get_channel(channellist[amount - 1])
            if amount > len(channellist):
                break
            if channel:
                embed = discord.Embed(title = 'C-5 공지', description = arg, color = (0xFF6060))
                await channel.send(embed = embed)
    else:
        return

@bot.command("병든앵무새")
async def 병든앵무새(ctx):
    return

@bot.command("앵무새")
async def 앵무새(ctx, *, arg):
    await ctx.send(arg)

@bot.command("반복")
async def 반복(ctx, *, arg):
    text = arg
    st = text.split(' ')
    print(st)
    wd = st[0]
    fg = st[1]
    hh = int(fg)
    print(wd)
    for i in range(hh):
        await ctx.send(wd)

@bot.command("동전뒤집기")
async def 동전뒤집기(ctx):
    amour = ctx.author.id
    if(os.path.isfile("/Coin_Toss/" + str(amour) + ".txt")):
        f = open("/Coin_Toss/" + str(amour) + ".txt", "r")
        money = f.read()
        amoney = int(money)
        #await ctx.send("ID: " + str(amour) + "\n보유 자금: " + money)
        coin = random.randrange(0, 2)
        if coin == 0:
            success = random.randrange(1, 11)
            if success >= 10:
                amoney += 50000
                f = open("/Coin_Toss/" + str(amour) + ".txt", "w")
                f.write(str(amoney))
                f.close()
                await ctx.send("대성공! + 50000 NS\n" + ctx.author.mention + "의 보유 자금: " + str(amoney) + " NS")
            else:
                amoney += 5000
                f = open("/Coin_Toss/" + str(amour) + ".txt", "w")
                f.write(str(amoney))
                f.close()
                await ctx.send("성공! + 5000 NS\n" + ctx.author.mention + "의 보유 자금: " + str(amoney) + " NS")
        if coin == 1:
            fail = random.randrange(1, 501)
            if fail >= 500:
                if amoney >= 60000:
                    amoney = 30000
                    f = open("/Coin_Toss/" + str(amour) + ".txt", "w")
                    f.write(str(amoney))
                    f.close()
                else:
                    amoney -= 30000
                    f = open("/Coin_Toss/" + str(amour) + ".txt", "w")
                    f.write(str(amoney))
                    f.close()
                await ctx.send("대실패!\n" + ctx.author.mention + "의 보유 자금: " + str(amoney) + " NS")
            else:
                amoney -= 3000
                f = open("/Coin_Toss/" + str(amour) + ".txt", "w")
                f.write(str(amoney))
                f.close()
                await ctx.send("실패... - 3000 NS\n" + ctx.author.mention + "의 보유 자금: " + str(amoney) + " NS")
    else:
        await ctx.send(ctx.author.mention + " 님은 회원이 아닙니다.\n `^^등록 동전뒤집기`를 통해 회원에 등록해주세요.")

@bot.command("등록")
async def 등록(ctx, *, arg):
    amour = ctx.author.id
    if arg == "동전뒤집기":
        f = open("/Coin_Toss/" + str(amour) + ".txt", "w")
        f.write("10000")
        f.close()
        await ctx.send(ctx.author.mention + " 회원 등록이 완료되었습니다.\n기본 자금 `10000`NS가 지급되었습니다.")
    if arg == "레벨":
        f = open("/Level/level/" + str(amour) + ".txt", "w")
        f.write("1")
        f.close()
        f = open("/Level/exp/" + str(amour) + ".txt", "w")
        f.write("0")
        f.close()
        f = open("/Level/requirement/" + str(amour) + ".txt", "w")
        f.write("210")
        f.close()
        await ctx.send(ctx.author.mention + " 회원 등록이 완료되었습니다.\n이제 레벨 기능을 사용할 수 있습니다.")
    else:
        await ctx.send("존재하지 않는 항목입니다.")

@bot.command("레벨")
async def 레벨(ctx):
    amour = ctx.author.id
    if(os.path.isfile("/Level/level/" + str(amour) + ".txt")):
        f = open("/Level/level/" + str(amour) + ".txt", "r")
        level = f.read()
        f.close()
        g = open("/Level/exp/" + str(amour) + ".txt", "r")
        exp = g.read()
        g.close()
        h = open("/Level/requirement/" + str(amour) + ".txt", "r")
        requirement = h.read()
        h.close()
        embed = discord.Embed(title="C-5 레벨", color=0xff6060, timestamp = ctx.message.created_at)
        embed.set_thumbnail(url=ctx.author.avatar),
        embed.set_footer(text=f'{ctx.author}이 요청함', icon_url=ctx.author.avatar)
        embed.add_field(name="레벨", value=level, inline=False)
        embed.add_field(name="EXP", value=exp + "/" + requirement, inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send(ctx.author.mention + " 님은 회원이 아닙니다.\n `^^등록 레벨`을 통해 회원에 등록해주세요.")

       
bot.run("YOUR TOKEN")

    
