import discord
from discord.ext import commands
import random
import time
import re
class 오락(commands.Cog):
    def __init__(self,bot):
        self.client=bot
    
    delList =  list()
    is_wordend = False
    wordDict = dict()
    alreadySet =  set()
    onewords = set()
    lastWord=''
    firstLetter=''
    nextWords=''
    firstTurn = False
    round = 0
    score = 0

    @commands.command(usage='(prefix)주사위',help='주사위를 굴려봅시다!     (prefix)주사위', aliases=['dice','DICE','Dice'])
    async def 주사위(self,ctx):
        randomNum= random.randrange(1,7)
        print(randomNum)
        if randomNum == 1:
            await ctx.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: :one:', colour=discord.Colour.red()))
        elif randomNum == 2:
            await ctx.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: :two:', colour=discord.Colour.blue()))
        elif randomNum == 3:
            await ctx.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: :three:', colour=discord.Colour.orange()))
        elif randomNum == 4:
            await ctx.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: :four:', colour=discord.Colour.gold()))
        elif randomNum == 5:
            await ctx.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: :five:', colour=discord.Colour.green()))
        else:
            await ctx.send(embed=discord.Embed(description='༼ つ ◕_◕ ༽つ :game_die: :six:', colour=discord.Colour.purple()))
    
    @commands.command(aliases=['8ball', 'test'], hidden=True)
    async def 질문받는다(self,ctx,*, question):
        response = ['확실해요',
                '아마.. 그럴걸요?',
                '아.. 잘 몰겠다',
                '그런 거 여기다 묻지 말고 지식인한테나 물어봐',
                '그으..거는 생각좀 해봐야 할듯']
        await ctx.send(f'질문: {question}\n답:{random.choice(response)}')

    @commands.command(aliases=['lottery', 'lotto'], help='복권을 긁어봅시다!     (prefix)복권',usage='(prefix)복권')
    async def 복권(self,ctx):
        number = [0]*7
        count = 0
        text=''
        for i in range(0,7):
            num= random.randrange(1,46)
            number[i] == num
            if count >=1:
                for i2 in range(0,i):
                    if number[i] == number[i2]:
                        numberText = number[i]
                        print("작동 이전값 : "+ str(numberText))
                        number[i] = random.randrange(1,46)
                        numberText = number[i]
                        print('작동 현재값 : ' + str(numberText))
                        if number[i] == number[i2]:
                            numberText = number[i]
                            print('작동 이전값 : ' + str(numberText))
                            number[i] = random.randrange(1,46)
                            numberText = number[i]
                            print('작동 현재값 : ' + str(numberText))
                            if number[i] == number[i2]:
                                await ctx.send('대단합니다!! 극적인 확률을 뚫고 숫자가 중복되었어요!')
            if count==6:
                text= text +' 보너스 숫자: '+str(number[i])
            else:
                count+=1
                text= text +' '+ str(number[i])
        await ctx.send(embed=discord.Embed(title=' ༼ つ ◕_◕ ༽つ', description=text, colour=discord.Color.red()))
    @commands.command()
    async def 동전뒤집기(self, ctx):
        coin = random.randint(0,100)
        if coin < 50:
            ctx.send('동전의 앞면이 나왔어요!')
        elif coin >50:
            ctx.send('동전의 뒷면이 나왔어요!')
        elif coin == 50:
            ctx.send('동전이 서버렸따!')
    @commands.command()
    async def 끝말잇기(self, ctx):
        global is_wordend
        global firstTurn
        global wordDict
        is_wordend = True
        firstTurn = True
        if firstTurn:
            with open('dict.txt', 'r', encoding="utf-8") as f:
                s= f.read()
            pat = re.compile('^[ㄱ-ㅎ가-힣]+$')
            for i in sorted([i for i in s.split() if pat.match(i) and len(i)>=2], key = lambda x: -len(x)):
                if i[0] not in 오락.wordDict:
                    오락.wordDict[i[0]] = set()
                오락.wordDict[i[0]].add(i)
            for i in 오락.wordDict:
                for j in 오락.wordDict[i]:
                    if j[-1] not in 오락.wordDict:
                        오락.delList.append(j)
            for j in 오락.delList:
                오락.onewords.add(j)
                오락.wordDict[j[0]].remove(j)
            await ctx.send('끝말잇기를 시작합니다')
    
    @commands.Cog.listener()
    async def on_message(self,message):
        global is_wordend
        global alreadySet
        global onewords
        global lastWord
        global firstLetter
        global nextWords
        global firstTurn
        global delList
        global round
        if is_wordend:
            if message.author.bot:
                pass
            else:
                firstLetter = message.content[0]

                if message.content == '포기':
                    await message.channel.send(f'이런 제가 이겼네요 ㅎㅎ')
                    is_wordend = False
                    await message.channel.send(f"{message.author.display_name} 님의 점수: {오락.score}")
                else:    
                    if firstTurn:
                        lastWord = random.choice(list(오락.wordDict[random.choice(list(오락.wordDict.keys()))]))
                        await message.channel.send(lastWord)
                        firstTurn = False
                    elif not firstTurn:
                        if firstLetter != lastWord[-1]:
                            await message.channel.send(lastWord[-1]+"(으)로 시작하는 단어를 입력하세요.")
                        elif message.content in 오락.onewords:
                            await message.channel.send('한방단어는 사용할 수 없습니다')
                        elif message.content in 오락.alreadySet:
                            await message.channel.send('이미 나온 단어입니다')
                        elif message.content not in 오락.wordDict.get(firstLetter, set()):
                            await message.channel.send('사전에 없는단어 입니다')
                        else:
                            if 오락.round >=20:
                                await message.channel.send("으앙 너무 잘하시네요 제가 졌어요")
                                await message.channel.send(오락.alreadySet)
                                await message.channel.send(f"{message.author.display_name} 님의 점수 : {오락.score}점")
                                is_wordend = False
                            else:
                                오락.alreadySet.add(message.content)
                                lastWord = message.content
                                nextWords = sorted(filter(lambda x: x not in 오락.alreadySet, 오락.wordDict[message.content[-1]]), key=lambda x:-len(x))[:random.randint(20,50)]
                                lastWord = nextWords[random.randint(0, random.randrange(0, len(nextWords)))]
                                count = 0
                                while True:
                                    if len(lastWord) <= 5:
                                        break
                                    else:
                                        lastWord = nextWords[random.randint(0, random.randrange(0, len(nextWords)))]
                                    count += 1
                                    if count> 100:
                                        break
                                    print(lastWord)
                                    print(count)
                                await message.channel.send(lastWord)  
                                오락.alreadySet.add(lastWord)
                                오락.score += len(message.content)
                                오락.round +=1

def setup(bot):
    bot.add_cog(오락(bot))