import discord
from discord.ext import commands
import os

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
        await message.channel.send("진짜 왜 그래?")
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
        embed = discord.Hyunta(colour=discord.Colour.red(), title="현타", description="싸이코임 무서워")
        embed.set_image(url=https://media.discordapp.net/attachments/801438907995521044/801481652827848764/image0.png)
        embed.set_thumbnail(url=https://cdn.discordapp.com/attachments/801469560921260045/801634321194025011/image0.png)
        await message.channel.send(embed=Hyunta)
    elif message.content == (f'{prefix}오클아 초대링크'):
        await message.channel.send("https://discord.com/oauth2/authorize?client_id=801291136093782046&scope=bot 이 링크로 초대")
    elif message.content == (f'{prefix}오클아 도배'):
        await message.channel.send("!warn")
    elif message.content == (f'{prefix}오클아 도움말'):
        embed = discord.Embed(colour=discord.Colour.green(), title="도움말", description="알아서 잘 쓰셈")
        embed.add_field(name="명령어 리스트", value="```?오클아 도움말, ?오클아, ?오클아 안녕, ?오클아 나 귀엽지?, ?오클아 나 섹시하지?, ?오클아 오클 귀엽지?, ?오클아 사랑해줘, ?오클아 원주율, ?오클아 똥, ?오클아 불만있음?, ?오클아 인공지능, ?오클아 현타는?, ?오클아 초대링크, ?오클아 도배```", inline=False)
        embed.add_field(name="봇 초대링크", value="https://discord.com/oauth2/authorize?client_id=801291136093782046&scope=bot", inline=False)
        embed.add_field(name="개발자 디스코드", value="```Trol1#1230```", inline=False)
        embed.add_field(name="개발자 깃헙 오픈소스", value="https://github.com/KawaiTrol1/discordbot", inline=False)
        embed.add_field(name="기획", value="오클", inline=False)
        embed.add_field(name="마지막 업데이트", value="```2021.1.21 (Beta 0.2.0)```", inline=False)
        await message.channel.send(embed=embed)

client.run(os.environ['token'])