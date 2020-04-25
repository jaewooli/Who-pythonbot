import asyncio, discord, random, requests
from discord.ext import commands, tasks
import os
from itertools import cycle
import json
import hanspell
from bs4 import BeautifulSoup, SoupStrainer
def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]

def surver():
    with open('prefixes.json','r') as f:
        surver= json.load(f)
    
    return len(surver)

token = "Hmm...?"
client = discord.Client()
bot = commands.Bot(command_prefix=get_prefix,description='여러 정보를 알려드리는 Who 봇입니다!!')
permission=discord.Permissions
bot.remove_command('help')
commands.HelpCommand(context='help 명령어로 명령어들을 확인해보세요!!')

Gamelist = cycle(['.도움말!!', '.help!!','SNS는 인생의 낭비',f'사용하고 있는 서버 : 총 {surver()}개'])

@tasks.loop(seconds=10.0)
async def Change_status():
    await bot.change_presence(activity=discord.Game(next(Gamelist)))


@bot.command(hidden=True)
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(embed=discord.Embed(title='명령어 에러!!',
        description=f'{ctx[1:]}이라는 명령어는 없습니다!\n\n .help를 이용해주세요!', color=discord.Color.green()))
@bot.command(aliases = ['멤버_생일'])
async def birthday(ctx):

    birthday = discord.Embed(title = f'{ctx.author}님의 생일은? 🎂',
    description = ctx.author.created_at.strftime("%Y년 %m월 %d일".encode("unicode-escape").decode()).encode().decode("unicode-escape"))

    await ctx.send(embed = birthday)

@bot.command(hidden=True)
async def load(ctx, extension):
    bot.load_extension(f'Cogs.{extension}')

@bot.command(hidden=True)
async def unload(ctx, extension):
    bot.unload_extension(f'Cogs.{extension}')

@bot.command(aliases=['이미지검색'])
async def searchimg(ctx,*, img):
    try:
        num=int(img[-1])
        img=img[:-1]
         
    except:
        num =0
    url= 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='+img
    print(url)
    params = {'query' : '파이썬'}
    header_info={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    response = requests.get(url, headers=header_info, params=params) 
    images = BeautifulSoup(response.content, 'lxml')
    images = images.find_all('img', class_='_img')
    data_images=[]
    for link in images:
        data_images.append(link.get('data-source'))
    embed= discord.Embed(name=img, color=discord.Color(0x72e3ef))
    embed.set_image(url=data_images[num])
    await ctx.send(embed=embed)

for filename in os.listdir('./Cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print('bot is ready')
    Change_status.start()


bot.run(token)