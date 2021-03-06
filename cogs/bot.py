from itertools import cycle

import discord
from discord.ext import commands, tasks


class Bot(commands.Cog):

    def __init__(self, client):
        self.client = client
        # Bot Status
        self.status = cycle(['as a Meow ^^~', 'meow meow'])

    # on_ready
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.idle, activity=discord.Game('Bot is ready'))
        print('Bot is ready.')
        self.change_status.start()

    # change_status
    # Tasks
    @tasks.loop(seconds=10)
    async def change_status(self):
        # Change Status of bot
        await self.client.change_presence(activity=discord.Game(next(self.status)))
    
    # stop
    # Commands
    @commands.command(aliases=['close','logout','l'])
    async def leave(self, ctx):
        await ctx.send('Bái bai')
        await self.client.close()
        await self.client.logout()
        print(f'Meow.')


def setup(client):
    client.add_cog(Bot(client))
