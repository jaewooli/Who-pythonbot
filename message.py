import discord
import random
import time
import datetime
import requests
import urllib, urllib.request
from bs4 import BeautifulSoup
from datetime import datetime # 날짜 구하는거
import os
import sys
import json
import youtube_dl
import re
import string
from discord.ext import commands
import time


token = "Hmm..?"
client = discord.Client()
user = discord.User
@client.event
async def on_ready():
    print("Token :", client.user.id)
    print("The bot has started")
    list_game=['.도와줘','안뇽!!','.help','안녕 여러분','SeX']
    game= discord.Game(list_game[1])
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def mentioned_in(message):
    await message.client.send(str(message.author)+'님이 당신을 언급했습니다!')

@client.event
async def on_message(message):
    if message.content.startswith(".안녕"):
        await message.channel.send(embed=discord.Embed(title="༼ つ ◕_◕ ༽つ", description="ToBOT의 도우미 ToBOT 입니다 \n 무엇을 도와드릴까요?", color=discord.Color.blue()))

    elif message.content == '.프로필':
        embed=discord.Embed(
            title=str(message.author)+'님의 프로필입니다',
            colour = discord.Colour.gold()
        )
        embed.add_field(name='이름:', value=str(message.author.display_name), inline=False)
        embed.add_field(name='ID:', value=str(message.author.id), inline=False) 
        embed.set_image(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    elif message.content.startswith(".잘가"):
        await message.channel.send(embed=discord.Embed(title="༼ つ ◕_◕ ༽つ", description="제가 필요하면 언제든지 다시 불러주세요.", color=discord.Color.blue()))

    elif message.content.startswith(".코딩운"):
        randnum = random.randrange(1, 3)
        if randnum == 1:
            await message.channel.send(embed=discord.Embed(title="༼ つ ◕_◕ ༽つ : 오늘 코딩은 뭔가 잘될거 같은데요?!", color=discord.Color.blue()))
        else:
            await message.channel.send(embed=discord.Embed(title="༼ つ ◕_◕ ༽つ : 흠.. 오늘은 쉬는게 어떤가요?", color=discord.Color.red()))

    elif message.content.startswith(".도와줘"):
        embed = discord.Embed(
            title = 'WhO 봇 에서 사용할 수 있는 명령어들 입니다.',
            description = '~~ 꼭 보세요 안그러면 후회합니다 ~~',
            colour = discord.Colour.blue()
        )
        
        embed.add_field(name = '.안녕', value = '이 명령어로 저와 인사할 수 있습니다!',inline = False)
        embed.add_field(name = '.잘가', value = '이 명령어로 저와 작별할 수 있습니다!',inline = False)
        embed.add_field(name = '.코딩운', value = '당신의 오늘 코딩운을 알려드려요!',inline = False)
        embed.add_field(name = '.모아니면도', value = '윷놀이 간접체험 해드립니다!',inline = False)
        embed.add_field(name = '.복권', value = '만약 오늘 당신의 운이 좋다면 한번 해보세요!\n 혹시 압니까? 1등이 될지!!', inline = False)
        embed.add_field(name = '.프로필', value = '당신의 프로필을 보여드려요!', inline= False)
        embed.add_field(name = '.디엠 (이름) (메세지)', value = 'WhO 봇이 누군가에게 대신 메세지를 보내드려요!\n그래도 걱정은 마세요. 누가 보낸지는 모를 겁니다')

        await message.channel.send(embed=embed)
        
    elif message.content.startswith(".모아니면도"):
        randnum = random.randrange(1, 6)
        if randnum == 1:
            await message.channel.send(embed=discord.Embed(title="༼ つ ◕_◕ ༽つ : 도!", color=discord.Color.blue()))
        elif randnum == 2:
            await message.channel.send(embed=discord.Embed(title="༼ つ ◕_◕ ༽つ : 개!", color=discord.Color.red()))
        elif randnum == 3:
            await message.channel.send(embed=discord.Embed(title="༼ つ ◕_◕ ༽つ : 걸!", color=discord.Color.red()))
        elif randnum == 4:
            await message.channel.send(embed=discord.Embed(title="༼ つ ◕_◕ ༽つ : 윷!", color=discord.Color.red()))
        elif randnum == 5:
            await message.channel.send(embed=discord.Embed(title="༼ つ ◕_◕ ༽つ : 모!", color=discord.Color.red()))
        else:
            await message.channel.send(embed=discord.Embed(title="༼ つ ◕_◕ ༽つ 오류가 있나봅니다 ??", color=discord.Color.red()))
        
    
    elif message.content.startswith(".복권"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7] # 배열크기 선언해줌
        count = 0
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("작동 현재값 : " + str(numberText))
                        if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title=" ༼ つ ◕_◕ ༽つ",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await message.channel.send(embed=embed)  
        
    elif message.content.startswith('.주사위'):

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await message.channel.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: '+ ':one:'))
        if randomNum == 2:
            await message.channel.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: ' + ':two:'))
        if randomNum ==3:
            await message.channel.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: ' + ':three:'))
        if randomNum ==4:
            await message.channel.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: ' + ':four:'))
        if randomNum ==5:
            await message.channel.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: ' + ':five:'))
        if randomNum ==6:
            await message.channel.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: ' + ':six: '))

    elif message.content.startswith('.genie'):
        headers = {'User-Agent' : 'Mozila/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        url= 'https://www.genie.co.kr/chart/top200'
        resp = requests.get(url, headers = headers)

        soup = BeautifulSoup(resp, 'html.parser')
        charts=soup.select('#body-content > div.newest-list > div.music-lis-wrap > table > tbody > tr')
        print(charts)
        embed=discord.Embed(
            title='현재 지니 차트입니다',
            colour=discord.Colour.from_rgb(33,170,216)
        )
        for song in charts:
            sing= song.find('td',{'class':'info'}).find('a', {'class': 'title ellipsis'}).text
            sing_artist= song.find('td',{'class':'info'}).find('a', {'class': 'artist ellipsis'}).text
            embed.add_field(name=sing, value=sing_artist, inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith(".마스크"):
        url_maskname = "https://search.shopping.naver.com/search/all.nhn?origQuery=%EB%A7%88%EC%8A%A4%ED%81%AC&spec=M10018852%7CM10811848&pagingIndex=1&pagingSize=40&viewType=list&sort=rel&frm=NVSHCAT&cat_id=50002057&query=%EB%A7%88%EC%8A%A4%ED%81%AC"
        req = urllib.request.urlopen(url_maskname)
        res = req.read()
        
        url_maskprice = "https://search.shopping.naver.com/search/all.nhn?origQuery=%EB%A7%88%EC%8A%A4%ED%81%AC&spec=M10018852%7CM10811848&pagingIndex=1&pagingSize=40&viewType=list&sort=rel&frm=NVSHCAT&cat_id=50002057&query=%EB%A7%88%EC%8A%A4%ED%81%AC"
        req = urllib.request.urlopen(url_maskprice)
        res = req.read()

        soup1 = BeautifulSoup(res,'html.parser') # BeautifulSoup 객체생성
        maskname = soup1.find_all('a',class_='link') # 데이터에서 태그와 클래스를 찾는 함수
        maskname = [each_line.get_text().strip() for each_line in maskname[:100]]

        soup2 = BeautifulSoup(res,'html.parser') # BeautifulSoup 객체생성
        maskprice = soup2.find_all('span',class_='num _price_reload') # 데이터에서 태그와 클래스를 찾는 함수
        maskprice = [each_line.get_text().strip() for each_line in maskprice[:100]]
        embed = discord.Embed(
            title = '현재 등록된 마스크 입니다',
            colour = discord.Colour.red()
        )
        for loop in range(0, 20):
            embed.add_field(name = maskname[loop], value = maskprice[loop] + "원",inline = False)

        await message.channel.send(embed=embed)

    elif 'TestMessage' in message.content:
        embed=discord.Embed(title='? 뭘 원하시는 거죠?', colour=discord.Colour.red())
        embed.set_image(url='https://mblogthumb-phinf.pstatic.net/20131114_72/adc0420_13844045260110PvWY_JPEG/%C0%E2%BE%D2%B4%D9_%BF%E4%B3%F0_01.JPG?type=w2')
        await message.delete()
        await message.channel.send(embed=embed)

    elif message.content.startswith(".개새"):
        await message.channel.send('어! 그딴 말은 어! 시땡 쓰면 안되는그야!')
        await message.delete()

    elif message.content.startswith('.야 후'):  
        randomNum=random.randint(0,1)
        if randomNum==0:
            await message.channel.send('https://www.yahoo.com/')
        elif randomNum==1:
            await message.channel.send('ㅔ?')

    elif message.content =='.아이디':                 
        await message.channel.send(message.author.id)       
    elif message.content == '.id':
        await message.channel.send(message.author.id)
    elif message.content =='.ID':
        await message.channel.send(message.author.id)
    
    elif message.content.startswith('.디엠 '):
        list=message.content.split(' ')
        author=message.guild.get_member_named(list[1])
        msg=' '.join(list[2:])
        await author.send(msg)
        await message.delete()
    
    elif message.content== '.서버정보':
        total_roles = len(message.guild.roles)
        embed=discord.Embed(title =message.guild.name+'의 정보입니다', colour=discord.Colour.blue())
        embed.set_thumbnail(url=message.guild.icon_url)
        embed.add_field(name='주인장', value=message.guild.owner.name)
        embed.add_field(name='서버 탄신일', value=message.guild.created_at)
        embed.add_field(name='역할 개수', value=total_roles)
        embed.add_field(name='멤버', value=message.guild.member_count)
        embed.add_field(name='채널 개수', value=str(len(message.guild.channels))+': 총 채널\n'+
            str(len(message.guild.text_channels))+':채팅 채널\n'+str(len(message.guild.voice_channels))+':음성 채널')
        embed.set_footer(text='ServerName:'+str(message.guild.name)+'|ServerID:'+str(message.guild.id))
        await message.channel.send(embed=embed)
    
    elif message.content.startswith('.밴'): #수정 필요
        list2=message.content.split(' ')
        try:
            if list2[1] == None:
                await message.channel.send(embed=discord.Embed(title='형식을 잘못 입력하셨네요!', 
                description='.밴 (유저) (밴 사유)\n__**주의※ 밴 자격이 없다면 밴을 할 수 없습니다!!**__', color=discord.Colour.red()))
            elif list2[2] == None:
                await message.channel.send(embed=discord.Embed(title='형식을 잘못 입력하셨네요!', 
                description='.밴 (유저) (밴 사유)\n__**주의※ 밴 자격이 없다면 밴을 할 수 없습니다!!**__', color=discord.Colour.red()))
            if message.author == message.guild.owner: 
                user=message.guild.get_member_named(list2[1])
                await user.send(user.name+'님은 '+message.guild.name+'에서 쫓겨나셨습니다... 흑')
                time.sleep(1)
                await message.guild.kick(user, reason=list2[2])
                await message.channel.send(embed =discord.Embed(description=list2[1]+'님이 밴을 당하셨어요~ 다시 들어올려면 ㅎㅎ 꽤 힘들겠네요', color=discord.Colour.red()))
        except:
            await message.channel.send(embed = discord.Embed(description='ㅇ? 오류가 났네요, '+message.author.name+'님이 권한을 가지고 있는지 확인해보세요!'))
    elif message.content =='.아바타':
        await message.channel.send('히어 유 아'+str(message.author.avatar_url))
@client.event
async def on_message_delete(message): 
     if message.author.bot == True:
        embed=discord.Embed(title='ㅋㅋ 야 누가 이거:arrow_down: 지웠는데?', color=discord.Color.red())
        embed.add_field(name='메세지:', value=message.content)
        await message.channel.send(embed=embed)
        

client.run(token)
