import json

import discord
from discord import client
from discord.ext import commands
from discord.ext.commands.core import has_permissions
from discord.utils import get


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.category_name = 'Gạp Phêm'
        self.channel_name = 'phim-đang-chiếu'
        self.voice_gap_1 = 'Gạp 1'
        self.voice_gap_2 = 'Gạp 2'
        self.role_name = 'Nhưn Diên Bán Hàng'
        self.prefix_file = './prefix.json'

    # welcome
    # Commands
    @commands.command(aliases=['hello', 'hi', 'w'])
    async def welcome(self, ctx):
        author_name = str(ctx.author).split('#')[0]
        await ctx.send(f'Oh welcome {author_name}')

    # auto
    # Commands
    @commands.command(aliases=['gen', 'g'])
    @commands.has_permissions(manage_channels=True)
    async def generate(self, ctx):
        self.author = ctx.author
        self.guild = ctx.message.guild
        self.category_permission = discord.PermissionOverwrite()
        self.channel_perrmission = discord.PermissionOverwrite()
        self.channel = get(self.guild.text_channels, name=self.channel_name)
        self.gap1 = get(self.guild.text_channels, name=self.voice_gap_1)
        self.gap2 = get(self.guild.text_channels, name=self.voice_gap_2)
        self.category = get(self.guild.categories, name=self.category_name)
        self.mrole = get(ctx.guild.roles, name=self.role_name)
        # Create category if category is not define
        if self.category is None:
            self.category = await self.guild.create_category(self.category_name)
            await ctx.send(f'Đã tạo {self.category}')

        # Create channel if channel is not define
        # Text Channel
        if self.channel is None:
            self.channel = await self.guild.create_text_channel(name=self.channel_name, category=self.category)
            await ctx.send(f'Đã tạo {self.channel} trong {self.category}')
        # Voice Channel
        if self.gap1 is None:
            self.gap1 = await self.guild.create_voice_channel(name=self.voice_gap_1, category=self.category)
            await ctx.send(f'Đã tạo {self.voice_gap_1} trong {self.category}')
        if self.gap2 is None:
            self.gap2 = await self.guild.create_voice_channel(name=self.voice_gap_2, category=self.category)
            await ctx.send(f'Đã tạo {self.voice_gap_2} trong {self.category}')

    @generate.error
    async def generate_error(self, ctx, error):
        if isinstance(error, discord.Forbidden):
            await ctx.send('Mài đéo có quyền :))')

    # on_member_join
    # Events
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined a server.')

    # on_guild_join
    # Events
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open(self.prefix_file, 'r') as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = '.'
        with open(self.prefix_file, 'w') as f:
            json.dump(prefixes, f, indent=4)

    # on_guild_remove
    # Events
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open(self.prefix_file, 'r') as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open(self.prefix_file, 'w') as f:
            json.dump(prefixes, f, indent=4)

    # on_member_remove
    # Events
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left a server.')

    # change_prefix
    # Commands
    @commands.command(aliases=['cp'])
    async def change_prefix(self, ctx, prefix):
        with open(self.prefix_file, 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open(self.prefix_file, 'w') as f:
            json.dump(prefixes, f, indent=4)

        await ctx.send(f'Channel {str(ctx.guild.name)} đổi prefix thành {prefix}.')

    # ping
    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Ping result: {round(self.client.latency *1000)}ms')

    # clear
    # Commands
    @commands.command(aliases=['purge', 'c'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=10):
        await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(Admin(client))
