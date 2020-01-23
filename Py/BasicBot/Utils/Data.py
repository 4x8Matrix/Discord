import discord, json

Config = json.loads(open("Config.json", "r").read())

def GetConfig():
    return Config