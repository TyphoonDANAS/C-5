# Work with Python 3.8
import asyncio
import discord
import random
import requests
import datetime
import openpyxl
from discord.ext import commands
import os

intents = discord.Intents.all()
game = discord.Game("^^도움말을 입력해주세요.")
bot = commands.Bot(command_prefix='^^', status=discord.Status.online, activity=game, help_command=None, intents=intents)
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
            if i not in memberlist:
                memberlist.append(i)
    while True:
        await bot.change_presence(activity=discord.Game("^^도움말을 입력해주세요."), status=discord.Status.online)
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(str(len(serverlist)) + "개의 서버", status=discord.Status.online))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Game(str(len(memberlist)) + "명의 사용자", status=discord.Status.online))
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

@bot.command("서버")
async def 서버(ctx, arg):
    if arg == "목록":
        list = []
        for guild in bot.guilds:
            list.append(guild.name)
        consequence = discord.Embed(title = 'C-5 서버 목록', description = '\n\n'.join(list) + "", color = (0xFF6060))
    await ctx.send(embed = consequence)

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
    channellist = [659072637569597482, 656882081946927166, 634344375845126154]
    amount = 0
    for i in range(len(channellist)):
        amount = amount + 1
        channel = bot.get_channel(channellist[amount])
        if amount > len(channellist):
            break
        if channel:
            embed = discord.Embed(title = 'C-5 공지', description = arg, color = (0xFF6060))
            await channel.send(embed = embed)

@bot.listen()
async def on_message(message):
    if message.author.bot:
        return None
    if message.content.startswith("") and message.author.id != 589471081354494012:
        file = openpyxl.load_workbook("레벨.xlsx")
        sheet = file.active
        exp = [100, 300, 600, 1000, 1500, 2100, 2800, 3600, 4500, 5500, 7000, 10000, 15000, 22500, 35000, 99999]
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                sheet["B" + str(i)].value = sheet["B" + str(i)].value + 4
                if sheet["B" + str(i)].value >= exp[sheet["C" + str(i)].value]:
                    sheet["C" + str(i)].value = sheet["C" + str(i)].value + 1
                    embed = discord.Embed(title = ':arrow_up:Level Up!', description = '현재 레벨: ' + str(sheet["C" + str(i)].value) + '\n현재 경험치: ' + str(sheet["B" + str(i)].value)) 
                    await message.channel.send(embed = embed)
                file.save("레벨.xlsx")
                break

            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 0
                sheet["C" + str(i)].value = 1
                file.save("레벨.xlsx")

                i += 1

                                                

@bot.command("병든앵무새")
async def 병든앵무새(ctx):
    return

@bot.command("앵무새")
async def 앵무새(ctx, arg):
    await ctx.send(arg)
    

bot.run('NTg5NDcxMDgxMzU0NDk0MDEy.XfJRWw.fMTsYTwslIRP_e88Kx7u5P3D_cg')
    
