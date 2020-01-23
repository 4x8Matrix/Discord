from discord.ext import commands
from Utils import Lists, Permissions, Cogs
import json, discord

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def help(self, ctx):
        pass
        
def setup(bot):
    bot.add_cog(Help(bot))