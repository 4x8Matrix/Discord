from discord.ext import commands
from Utils import Lists, Permissions, Cogs
import json, discord

class Sec(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, Ammount:int):
        await ctx.channel.purge(limit=Ammount, bulk=True)
        await ctx.send(f"> Deleted {Ammount} of message(s)", delete_after=2.5)

    @commands.command(pass_context=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, Member:discord.Member, *, Reason:str):
        await Member.kick(reason=Reason)

    @kick.on_error()
    
        
    @commands.command(pass_context=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, Member:discord.Member, *, Reason:str):
        await Member.ban(reason=Reason)
        
def setup(bot):
    bot.add_cog(Sec(bot))