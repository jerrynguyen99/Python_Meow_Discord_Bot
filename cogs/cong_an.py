import discord
from discord.ext import commands
from discord.ext.commands.errors import MemberNotFound, MissingPermissions


class CongAn(commands.Cog):

    def __init__(self, client):
        self.client = client

    # kick
    # Commands
    @commands.command(aliases=['kick', 'k'])
    async def _kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send(f'Bái bai, {member}')
        await commands.kick(member, reason=reason)

    # kick
    # Handle Error
    @_kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Cho tao cái tên.')
        if isinstance(error, MemberNotFound):
            await ctx.send('Tao không biết thằng này.')
        if isinstance(error, MissingPermissions):
            await ctx.send('Nó be quá tao chơi hông lại.')

    # ban
    # Commands
    @commands.command(aliases=['ban', 'b'])
    async def _ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.send(f'{member}, Mài bị ban rồi con, bye mài: {reason}')
        await member.ban(reason=reason)

    @_ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Mài muốn cấm thằng nào.')

    # unban
    # Commands
    @commands.command(aliases=['unban', 'ub'])
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
