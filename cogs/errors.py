import discord
from discord.ext import commands

class Errors(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    # Command not Found 
    # Errors
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            print('Bot said: Lam gi co')
            await ctx.send(f'Làm gì có :)))') 


    
def setup(client):
    client.add_cog(Errors(client))