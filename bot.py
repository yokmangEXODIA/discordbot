import discord
from discord.ext import commands
import os
import datetime

client = commands.Bot(command_prefix = '-')
prefix = "?"

@client.event
async def on_ready():

  # [discord.Status.online = 온라인],[discord.Status.idle = 자리비움],[discord.Status.dnd = 다른용무],[discord.Status.offline = 오프라인]
  await client.change_presence(status=discord.Status.idle)

  await client.change_presence(activity=discord.Game(name="?오클아 도움말"))
  #await client.change_presence(activity=discord.Streaming(name="스트림 방송중", url='링크'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="노래 듣는중"))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="영상 시청중"))
  
  print("봇 이름:",client.user.name,"봇 아이디:",client.user.id,"봇 버전:",discord.__version__)

@client.event 
async def on_message(message):
    if message.content == (f'{prefix}오클아'):
        await message.channel.send("ㅙ?")
    elif message.content == (f'{prefix}오클아 안녕'):
        await message.channel.send("안녕 못함")
    elif message.content == (f'{prefix}오클아 나 귀엽지?'):
        await message.channel.send("너 개같이 생겼어~^^")
    elif message.content == (f'{prefix}오클아 나 섹시하지?'):
        await message.channel.send("이자슥 딱대 넌 손절이다")
    elif message.content == (f'{prefix}오클아 오클 귀엽지?'):
        await message.channel.send("진짜 우주 최강 귀요미다")
    elif message.content == (f'{prefix}오클아 사랑해줘'):
        await message.channel.send("특별히 내가 사랑해줄께")
    elif message.content == (f'{prefix}오클아 원주율'):
        await message.channel.send("? 수학 싫음 에엑따")
    elif message.content == (f'{prefix}오클아 똥'):
        await message.channel.send("응 니얼굴~")
    elif message.content == (f'{prefix}오클아 불만있음?'):
        await message.channel.send("물도있음")
    elif message.content == (f'{prefix}오클아 인공지능'):
        await message.channel.send("나는 인공지능 삐리비리삑!")
    elif message.content == (f'{prefix}오클아 누가 천재임?'):
        await message.channel.send("일단 적어도 넌 아님")
    elif message.content == (f'{prefix}오클아 현타는?'):
        Hyunta = discord.Embed(colour=discord.Colour.red(), title="현타", description="싸이코임 무서워")
        Hyunta.set_image(url="https://cdn.discordapp.com/attachments/801469560921260045/801481891521364058/image0.png")
        Hyunta.set_thumbnail(url="https://cdn.discordapp.com/attachments/801469560921260045/801634321194025011/image0.png")
        await message.channel.send(embed=Hyunta)
    elif message.content == (f'{prefix}오클아 내정보'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        tmi = discord.Embed(colour=discord.Colour.blue())
        tmi.add_field(name="이름", value=message.author.name, inline=True)
        tmi.add_field(name="서버이름", value=message.author.display_name, inline=True)
        tmi.add_field(name="가입일", value=str(date.year) + "년 " + str(date.month) + "월 " + str(date.day) + "일 ", inline=True)
        tmi.add_field(name="아이디", value=message.author.id, inline=True)
        tmi.set_thumbnail(url=message.author.avarta_url)
        await message.channel.send(embed=tmi)
    elif message.contnet == (f'{prefix}오클아 서버'):
        await message.channel.send("서버가 뭐지 먹는건가")
    elif message.content == (f'{prefix}오클아 현재시간'):
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        f = datetime.datetime.today().second
        await message.channel.send(str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초 " + "다 이자슥아")
    elif message.content == (f'{prefix}오클아 초대링크'): 
        await message.channel.send("https://discord.com/oauth2/authorize?client_id=801316073508438016&scope=bot 이 링크로 초대")
    elif message.content == (f'{prefix}오클아 도배'):
        await message.channel.send("!warn")
    elif message.content == (f'{prefix}오클아 도움말'):
        embed = discord.Embed(colour=discord.Colour.green(), title="도움말", description=" ")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/801469560921260045/801767533110755358/kasjdfklajskldfjklajsdf.png")
        embed.add_field(name="명령어 리스트", value="https://docs.google.com/document/d/15_S6TZz1II7DSzn6CLD_SpdL8S9VxGcUKasasygkGFI/edit?usp=sharing", inline=True)
        embed.add_field(name="봇 초대링크", value="https://discord.com/oauth2/authorize?client_id=801316073508438016&scope=bot", inline=True)
        embed.add_field(name="개발자 디스코드", value="```Trol1#1230```", inline=True)
        embed.add_field(name="개발자 깃헙 오픈소스", value="https://github.com/KawaiTrol1/discordbot", inline=True)
        embed.add_field(name="마지막 업데이트", value="```2021.1.21 (Beta 0.3.1)```", inline=True)
        await message.channel.send(embed=embed)

client.run(os.environ['token'])