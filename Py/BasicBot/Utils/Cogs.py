from discord.ext import commands
import discord

def Cog_Exist(Bot, Cog_Name):
    
    if Bot.get_cog(Cog_Name) == None:
        return False
    else:
        return True

def get_cog(Bot, Cog_Name):
    
    if Cog_Exist(Bot, Cog_Name):
        return Bot.get_cog(Cog_Name)
    else:
        return False

def get_commands(Bot, Cog_Name):
    
    if Cog_Exist(Bot, Cog_Name):
        cog = Bot.get_cog(Cog_Name)
        commands = cog.get_commands()
        return commands
    else:
        return False

def unload_cog(Bot, Cog_Name):
    
    if Cog_Exist(Bot, Cog_Name):
        try:
            Bot.unload_extension(Cog_Name)
            return False
        except:
            return True
    else:
        return False

def load_cog(Bot, Cog_Name):
    
    if Cog_Exist(Bot, Cog_Name):
        try:
            Bot.load_extension(Cog_Name)
            return False
        except:
            return True
    else:
        return False
    
