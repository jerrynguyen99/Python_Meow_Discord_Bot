import discord
import os
from discord.ext import commands

default_prefix = '.'
client = commands.Bot(command_prefix=default_prefix)

@client.command()
async def load(ctx, extension):
    print(f'Load: cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    print(f'Unload: cogs.{extension}')
    client.unload_extension(f'cogs.{extension}')

# Load from extension from osdir
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run('NzgyOTAzNDc5OTQ5MTk3MzMy.X8S9rw.nNi1hX-YVfskSBEI78XWmxyv1U4')


