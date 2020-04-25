import discord
from discord.ext import commands
import json

class 상태(commands.Cog):
    def __init__(self, bot):
        self.client=bot

    @commands.command(usage='(prefix)ping', help='지금 네트웤 상태를 알아봐요!      (prefix)ping')
    async def ping(self,ctx):
        await ctx.send(f'Pong!   {round(ctx.latency * 1000)}ms')

    @commands.command(aliases=['bot'], usage='(prefix)봇',help='서버에 있는 봇들을 봐봅시다     (prefix)봇')
    async def 봇(self,ctx):
        bot_list=[member for member in ctx.guild.members if member.bot == True]
        bot_list=[name.display_name for name in bot_list]
        bot_list.sort()
        embed=discord.Embed(description='', colour= discord.Color.red())
        for bot in bot_list:
            embed.add_field(name='', value=f'{bot}')
        await ctx.send(embed=embed)
    
    @commands.command(hidden=True)
    async def 서버(self,ctx):
        await ctx.send(f'{ctx.guild.region}')

    @commands.command(aliases=['Id', 'id', 'ID'], hidden=True)
    async def 아이디(self,ctx):
        await ctx.send(ctx.author.id)

    @commands.command(hidden=True)
    async def 상태(self,ctx, member : discord.Member = None):
        statuses = {'online': "온라인", "idle": "자리비움", "dnd": "다른 용무 중", "offline": "오프라인"}
        embed=discord.Embed(title='member Status')
        status=statuses[f'{member.status}']
        embed.add_field(name = '유저 상태', value = str(status), inline = False)
        await ctx.send(embed=embed)

    @commands.command(aliases=['서버정보','surverinfo'],usage='(prefix)server ')
    async def server(self,ctx):
        embed=discord.Embed(title=f'{ctx.author.guild.name}',color=discord.Color(0x798CDF))
        embed.set_thumbnail(url=ctx.author.guild.icon_url)
        embed.set_footer(text=f'요청자 : {ctx.author.name}', icon_url= ctx.author.avatar_url)
        embed.add_field(name='멤버 수', value=len(ctx.author.guild.members), inline=False)
        embed.add_field(name='아이디', value=ctx.author.guild.id, inline=False)
        embed.add_field(name='서버 위치', value=ctx.author.guild.region, inline=False)
        embed.add_field(name='강제 채널', value=ctx.author.guild.afk_channel, inline=False)
        embed.add_field(name='보안 수듄', value=ctx.author.guild.verification_level, inline=False)
        embed.add_field(name='총 채널 개수', value=len(ctx.author.guild.channels), inline=False)
        embed.add_field(name='음성 채널 수', value=len(ctx.author.guild.voice_channels), inline=False)
        embed.add_field(name='채팅 채널 수', value=len(ctx.author.guild.text_channels),inline=False)
        await ctx.send(embed=embed)


    @commands.command(aliases=['정보'], usage='(prefix)info 유저[자유]', help='당신의 정보를 확인하세요!!    (prefix)info 유저[자유]')
    async def info(self,ctx,info=None):
        a=' '
        statuses = {'online': "온라인", "idle": "자리비움", "dnd": "다른 용무 중", "offline": "오프라인"}
        for role in ctx.author.roles:
            role = role.name
            if role == '@everyone':
                continue
            a += role+' '
        if info != None:
            A=ctx.author.guild.get_member_named(info)
            print(type(A))
            print(A)
            ctx.author = A
            embed = discord.Embed(title=ctx.author.name, color = discord.Color(0x5AD2FF), timestamp= ctx.message.created_at)
            status=statuses[f'{ctx.author.status}']
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f'요청자 : {ctx.author.name}', icon_url=ctx.author.avatar_url)
            embed.add_field(name = '유저 상태', value = str(status), inline = False)
            embed.add_field(name='아이디', value=ctx.author.id, inline=False)
            embed.add_field(name='닉네임', value=ctx.author.display_name, inline=False)
            embed.add_field(name='들어온 날짜', value=ctx.author.joined_at, inline=False)
            embed.add_field(name='계정 생성 날짜', value=ctx.author.created_at, inline=False)
            embed.add_field(name='폰 여부', value=ctx.author.is_on_mobile(), inline=False)
            embed.add_field(name='역할', value=a, inline=False)
            embed.add_field(name='활동', value=ctx.author.activity, inline=False)
            embed.add_field(name='봇 여부', value= ctx.author.bot, inline=False)
            await ctx.send(embed=embed)
        elif info == None:
            print('None')
            embed = discord.Embed(title=ctx.author.name, color = discord.Color(0x5AD2FF), timestamp= ctx.message.created_at)
            status=statuses[f'{ctx.author.status}']
            embed.set_thumbnail(url=ctx.author.avatar_url)
            embed.set_footer(text=f'요청자 : {ctx.author.name}', icon_url=ctx.author.avatar_url)
            embed.add_field(name = '유저 상태', value = str(status), inline = False)
            embed.add_field(name='아이디', value=ctx.author.id, inline=False)
            embed.add_field(name='닉네임', value=ctx.author.display_name, inline=False)
            embed.add_field(name='들어온 날짜', value=ctx.author.joined_at, inline=False)
            embed.add_field(name='계정 생성 날짜', value=ctx.author.created_at, inline=False)
            embed.add_field(name='폰 여부', value=ctx.author.is_on_mobile(), inline=False)
            embed.add_field(name='역할', value=a, inline=False)
            embed.add_field(name='활동', value=ctx.author.activity, inline=False)
            embed.add_field(name='봇 여부', value= ctx.author.bot, inline=False)
            await ctx.send(embed=embed)        
    @info.error
    async def info_error(self, ctx, error): 
        with open('prefixes.json','r') as f:
                prefixes = json.load(f)
                prefix =prefixes[str(ctx.author.guild.id)]
        if isinstance(error, AttributeError):
            await ctx.send(embed=discord.Embed(title='명령어 에러!!'), description=f'이런... 이름은 잘 입력하셨나요?\n \
                {prefix}info (유저)\n ※유저를 입력하지 않으면 자신의 정보가 출력됩니다', color=discord.Color.red())
def setup(bot):
    bot.add_cog(상태(bot))
