import discord
from discord.ext import commands

class CongAn(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    #Commands
    @commands.command(aliases=['kick','k'])
    async def _kick(self, ctx, member : discord.Member, *, reason=None):
        await ctx.send(f'Say goodbye, {member}')
        await member.kick(reason=reason)
        
    #Commands
    @commands.command(aliases=['ban','b'])
    async def _ban(self, ctx,member : discord.Member, *, reason=None):
        await ctx.send(f'{member}, You have been banned. Due to: {reason}')
        await member.ban(reason=reason)

    #Commands
    @commands.command(aliases=['unban','ub'])
    async def _unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, memberr_discriminator = member.split('#')

        for banned_user in banned_users:
            user = banned_user.user
            
            if (user.name, user.discriminator) == (member_name, memberr_discriminator):
                await ctx.send(f'{member_name}, You have been unbanned.')
                await ctx.guild.unban(user)
                return

def setup(client):
    client.add_cog(CongAn(client))