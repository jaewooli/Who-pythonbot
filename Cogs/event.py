import discord
from discord.ext import commands, tasks
import json, re, random
def readprefix(ctx):
        with open('prefixes.json','r') as f:
            prefixes = json.load(f)
            prefix =prefixes[str(ctx.author.guild.id)]
            return prefix
class Event(commands.Cog):
    def __init__(self,bot):
        self.client=bot
    
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print('{} 이(가) 서버에서 나갔습니다'.format(member))

    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f'{member} 이(가) 서버에 들어왔습니다.')
    


def setup(bot):
    bot.add_cog(Event(bot))