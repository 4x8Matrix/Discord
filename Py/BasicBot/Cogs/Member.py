from discord.ext import commands
from Utils import Lists, Permissions, Cogs
from googletrans import Translator
from random_word import RandomWords
import json, discord

LanguageClient = Translator()

class Member(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        Message = await ctx.send("Pong!")
        await Message.edit(content=f"Pong! {str(commands.Bot.latency)}")

    @commands.command(pass_context=True)
    async def teach(self, ctx):
        English = RandomWords().get_random_word()
        Spanish = LanguageClient.translate(English, dest='es').text

        embed=discord.Embed(title="Teaching spanish!")
        embed.add_field(name="English", value=f"{English}", inline=True)
        embed.add_field(name="Spanish", value=f"{Spanish}", inline=True)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def language(self, ctx, *, Message:str):
        Data = LanguageClient.detect(Message)
        Data_2 = LanguageClient.translate(Message, dest='en')
        embed=discord.Embed(title="Detect language!")
        embed.add_field(name=f"{Data.lang}", value=f"{Message}", inline=True)
        embed.add_field(name="English", value=f"{Data_2.text}", inline=True)
        embed.set_footer(text=f"{Data.confidence}% sure.")
        await ctx.send(embed=embed)
    
    @commands.command(pass_context=True)
    async def learn(self, ctx, *, Message:str):
        embed=discord.Embed(title="Learning spanish.")
        embed.add_field(name="English", value=f"{Message}", inline=True)
        embed.add_field(name="Spanish", value=f"{LanguageClient.translate(Message, dest='es').text}", inline=True)
        await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    async def test(self, ctx):
        pass

        
        
def setup(bot):
    bot.add_cog(Member(bot))