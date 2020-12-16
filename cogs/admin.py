import discord
from discord import client
from discord.ext import commands

class Admin(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        #Change Status of bot
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('as a Meow ^^~ '))
        print('Bot is ready.')

    #Events
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined a server.')

    #Events
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server.')

    #Commands
    @commands.command()
    async def ping(self, ctx): 
        await ctx.send(f'Ping result: {round(self.client.latency *1000)}ms')

    #Commands
    @commands.command(aliases=['hello','hi','welcome','w'])
    async def _welcome(self, ctx):
        author_name = str(ctx.author).split('#')[0]
        await ctx.send(f'Oh welcome {author_name}')

    #Commands
    @commands.command(aliases=['clear','purge','c'])
    async def _clear(self, ctx,amount = 5):
        await ctx.channel.purge(limit=amount)

def setup(client):
    client.add_cog(Admin(client))