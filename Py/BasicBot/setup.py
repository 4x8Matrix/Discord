import sys, asyncio, json, os, discord
from discord.ext import commands
from Utils import Notification

Config = json.loads(open("Config.json", "r").read())

Bot = commands.Bot(command_prefix=Config["BotData"]["Prefix"], case_insensitive=True)
Bot.remove_command("help")

for File in os.listdir(os.getcwd()+"\\Cogs"):
    if str(File)[-3:] == ".py":
        try:
            Bot.load_extension("cogs."+str(File)[:-3])
        except Exception as e:
            print("{}:\n {}".format("cogs."+str(File)[:-3], e))

try:
    Bot.run(Config["BotData"]["Token"], reconnect=True)
except Exception as E:
    if E.__class__ == discord.errors.LoginFailure:
        print("Discord login failure.")
