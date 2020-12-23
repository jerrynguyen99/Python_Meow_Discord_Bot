import discord
from discord.ext import commands
from discord.ext.commands.core import has_permissions
from discord.utils import get


class Cinema(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.channel_name = 'phim-đang-chiếu'

    # auto
    # Commands
    @commands.command(aliases=['ns', 'nows', 'now'])
    @commands.has_permissions(manage_channels=True)
    async def now_showing(self, ctx):
        print('this command can run')


def setup(client):
    client.add_cog(Cinema(client))
