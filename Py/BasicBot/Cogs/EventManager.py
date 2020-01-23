import datetime, discord, asyncio, random
from discord.ext import commands
from Utils import Lists

class EventHandler(commands.Cog):
    def __init__(self, bot):
        self.Bot = bot
        return

    @commands.Cog.listener()
    async def on_ready(self):
        print("-"*25+"\n{}#{}\n{}\n".format(self.Bot.user.name, self.Bot.user.discriminator, datetime.datetime.now())+"-"*25)

        async def status_task():
                while True:
                    await self.Bot.change_presence(status=discord.Status.dnd, activity=discord.Game(" on {}".format(random.choice(Lists.GetGames()))))
                    await asyncio.sleep(60)

        self.Bot.loop.create_task(status_task())

    @commands.Cog.listener()
    async def on_command(self, ctx):
        print("{} --> {}".format(ctx.author, ctx.message.content))

def setup(bot):
    bot.add_cog(EventHandler(bot))

