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
fr = "^^"

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
            #if i not in memberlist:
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
                                    '\n**^^병든앵무새**: 말을 이상하게 따라합니다.', color = (0xFF6060))
        await ctx.author.send(embed = consequence)
    if arg == "기본":
        consequence = discord.Embed(title = 'C-5 기본 도움말', description = '**^^핑**: 핑을 알려줍니다.(ms)\n**^^계산**: 식을 계산합니다.', color = (0xFF6060))
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
    consequence = discord.Embed(title = 'C-5 버전: 1.6.2', description = 'Typhoon Code: Danas', color = (0xFF6060))
    await ctx.send(embed = consequence)

@bot.command("삭제")
async def 삭제(ctx, amount : int):
    if ctx.author.id == 416226495640502273:
        msg = amount + 1
        await ctx.channel.purge(limit = msg)
        await ctx.send(str(amount) + "개의 메시지가 삭제되었습니다.")
        await asyncio.sleep(2)
        await ctx.channel.purge(limit = 1)
    else:
        await ctx.send("제작자느님만 사용하실수잇는 명령어임니다.ㅅㄱ")

@bot.command("서버")
async def 서버(ctx, arg):
    if arg == "목록":
        list = []
        for guild in bot.guilds:
            list.append(guild.name)
        consequence = discord.Embed(title = 'C-5 서버 목록', description = '\n\n'.join(list) + "", color = (0xFF6060))
    await ctx.send(embed = consequence)

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
    user_id_list = [474952774497468416]
    for user_id in user_id_list:
        user = bot.get_user(user_id)
        for i in range(10):
            if ctx.author.id == 416226495640502273:
                await user.send('82kg 김치영 꼭! 읽어주세요~')
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
    if(os.path.isfile("C:/Users/user/Desktop/Bot_Dictionary/" + wd + ".txt")):
            await ctx.send("이미 배운 단어입니다.")
            return
    else:
        f = open("C:/Users/user/Desktop/Bot_Dictionary/" + wd + ".txt", "w")
        f.write(mn + "\n```" + str(ctx.author) + " 님이 알려주셨어요!```")
        f.close()
        await ctx.send("단어 " + wd + "을(를) 배웠습니다.")
        return

@bot.command("단어")
async def 단어(ctx, *, arg):
    channellist = [823821886185406525]
    channel = bot.get_channel(channellist[0])
    if channel:
        await channel.send(ctx.author.mention + "ㅈ까")
    else:
        try:
                text = arg
                if(os.path.isfile("C:/Users/user/Desktop/Bot_Dictionary/" + text + ".txt")):
                    f = open("C:/Users/user/Desktop/Bot_Dictionary/" + text + ".txt", "r")
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
        channellist = [770823719122894871, 770823719122894871]
        amount = 0
        for i in range(len(channellist)):
            amount = amount + 1
            channel = bot.get_channel(channellist[amount])
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


@bot.command("덱")
async def 덱(ctx, *, arg):
    common = ['불', '전기', '바람', '얼음', '독', '고장난', '도박', '잠금', '쇠']
    rare = ['에너지', '활', '가시', '제물', '광산', '빛', '균열', '크리티컬', '도박 성장']
    epic = ['레이저', '개조된 전기', '강풍', '기어', '파동', '화염', '돌', '죽음', '텔레포트', '감염', '흡수', '스위치', '회복', '복제', '빈 선물', '적응', '고장난 성장', '스피드건']
    legendary = ['핵', '빛의 검', '태양', '원자', '총', '태풍', '콤보', '별', '태극', '지뢰', '전이', '모래', '조커', '지옥', '방패', '눈보라', '성장', '소환', '암살', '양분', '시간', '달', '흐름', 'ix10', '침묵', '로얄', '조준경']
    all = ['불', '전기', '바람', '얼음', '독', '고장난', '도박', '잠금', '쇠','에너지', '활', '가시', '제물', '광산', '빛', '균열', '크리티컬', '도박 성장', '레이저', '개조된 전기', '강풍', '기어', '파동', '화염', '돌', '죽음', '텔레포트', '감염', '흡수', '스위치', '회복', '복제', '빈 선물', '적응', '고장난 성장', '현상금', '스피드건', '핵', '빛의 검', '태양', '원자', '총', '태풍', '콤보', '별', '태극', '지뢰', '전이', '모래', '조커', '지옥', '방패', '눈보라', '성장', '소환', '암살', '양분', '시간', '달', '흐름', 'ix10', '침묵', '로얄', '조준경']
    choicec = random.choice(all[:9])
    choicer = random.choice(all[9:18])
    choicee = random.choice(all[18:36])
    choicel = random.choice(all[36:])
    choicea = random.choice(all)
    cvalue = all.index(choicec)
    rvalue = all.index(choicer)
    evalue = all.index(choicee)
    lvalue = all.index(choicel)
    avalue = all.index(choicea)
    if arg == "생성":
        amount = 0
        clist = []
        clist.append(choicec)
        clist.append(choicer)
        clist.append(choicee)
        clist.append(choicel)
        while True:
            if choicea not in clist:
                amount = amount + 1
                clist.append(choicea)
                print(clist)
                if amount == 1:
                    embed = discord.Embed(title = 'C-5 랜덤다이스 덱 생성기', description = str(clist[0]) + " 주사위\n " + str(clist[1]) + " 주사위\n " + str(clist[2]) + " 주사위\n " + str(clist[3]) + " 주사위\n " + str(clist[4]) + " 주사위", color = (0xff6060))
                    await ctx.send(embed = embed)
                    clist.clear()
                    break
    if arg == "생성 일반":
        clist = []
        amount = 0
        random.shuffle(common)
        pickco = random.randrange(1, 10)
        pickcommon = str(common[pickco])
        for pickcommon in common:
            if pickcommon not in clist:
                amount = amount + 1
                clist.append(pickcommon)
                if amount == 5:
                    embed = discord.Embed(title = 'C-5 랜덤다이스 덱 생성기', description = str(clist[0]) + " 주사위\n " + str(clist[1]) + " 주사위\n " + str(clist[2]) + " 주사위\n " + str(clist[3]) + " 주사위\n " + str(clist[4]) + " 주사위", color = (0xff6060))
                    await ctx.send(embed = embed)
                    clist.clear()
                    break
    if arg == "생성 희귀":
        clist = []
        amount = 0
        random.shuffle(rare)
        pickco = random.randrange(1, 10)
        pickcommon = str(rare[pickco])
        for pickcommon in rare:
            if pickcommon not in clist:
                amount = amount + 1
                clist.append(pickcommon)
                if amount == 5:
                    embed = discord.Embed(title = 'C-5 랜덤다이스 덱 생성기', description = str(clist[0]) + " 주사위\n " + str(clist[1]) + " 주사위\n " + str(clist[2]) + " 주사위\n " + str(clist[3]) + " 주사위\n " + str(clist[4]) + " 주사위", color = (0xff6060))
                    await ctx.send(embed = embed)
                    clist.clear()
                    break
    if arg == "생성 영웅":
        clist = []
        amount = 0
        random.shuffle(epic)
        pickco = random.randrange(1, 18)
        pickcommon = str(epic[pickco])
        for pickcommon in epic:
            if pickcommon not in clist:
                amount = amount + 1
                clist.append(pickcommon)
                if amount == 5:
                    embed = discord.Embed(title = 'C-5 랜덤다이스 덱 생성기', description = str(clist[0]) + " 주사위\n " + str(clist[1]) + " 주사위\n " + str(clist[2]) + " 주사위\n " + str(clist[3]) + " 주사위\n " + str(clist[4]) + " 주사위", color = (0xff6060))
                    await ctx.send(embed = embed)
                    clist.clear()
                    break
    if arg == "생성 전설":
        clist = []
        amount = 0
        random.shuffle(legendary)
        pickco = random.randrange(1, 28)
        pickcommon = str(legendary[pickco])
        for pickcommon in legendary:
            if pickcommon not in clist:
                amount = amount + 1
                clist.append(pickcommon)
                if amount == 5:
                    embed = discord.Embed(title = 'C-5 랜덤다이스 덱 생성기', description = str(clist[0]) + " 주사위\n " + str(clist[1]) + " 주사위\n " + str(clist[2]) + " 주사위\n " + str(clist[3]) + " 주사위\n " + str(clist[4]) + " 주사위", color = (0xff6060))
                    await ctx.send(embed = embed)
                    clist.clear()
                    break
    if arg == "제외":
        await ctx.send("111%병신")


@bot.command("전직")
async def 전직(ctx, member: discord.Member=None):
    member = ctx.message.author
    await member.add_roles(get(ctx.guild.roles, name="신들의 영역"))
    await ctx.send(str(member) + ", 너도 할 수 있어")
             

@bot.command("채널따먹기")
async def 채널따먹기(ctx, channel_name):
    if ctx.author.id == 416226495640502273:
        guild = ctx.message.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        print(existing_channel)
        if existing_channel is not None:
            await existing_channel.delete()
        else:
            await ctx.send(f'No channel named, "{channel_name}", was found')
    else:
        await ctx.send("니 몇살인데")

@bot.command("홍보")
async def 홍보(ctx, member : discord.Member):
    if ctx.author.id == 416226495640502273:
        print(ctx.author)
        while True:
            await ctx.send(member.mention + "봇을 초대하고 싶다면: https://discord.com/api/oauth2/authorize?client_id=589471081354494012&permissions=8&scope=bot 으로")
    else:
        await ctx.send("반말하지마라")



"""
@bot.command("레벨")
async def 레벨(ctx, member : discord.Member):
    file = openpyxl.load_workbook("레벨.xlsx")
    sheet = file.active
    exp = [210, 315, 476, 707, 1064, 1596, 2394, 3591, 5383, 8071]
    i = 1
    while True:
        if sheet["A" + str(i)].value == str(member.id):
            level = str(sheet["C" + str(i)].value)
            ghk = str(sheet["B" + str(i)].value)
            embed = discord.Embed(title="C-5 레벨", description="C-5가 있는 서버에서의 총 활동량을 표시합니다.", color=0xff6060)
            embed.add_field(name="레벨", value = level, inline=False)
            embed.add_field(name="경험치", value = ghk + "/" + str(exp[int(level) - 1]), inline=False)
            await ctx.send(embed = embed)
            break

        i += 1
"""

        
bot.run('token')

    
