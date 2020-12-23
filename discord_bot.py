import json
import os

import discord
from discord.ext import commands


def get_prefix(client, message):
    with open('prefix.json', 'r') as prefix_file:
        prefixes = json.load(prefix_file)
    # print("Current prefix: ",prefixes[str(message.guild.id)])
    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix)


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

token_file = open('./token', 'r')
token = (token_file.read())
client.run(token)
