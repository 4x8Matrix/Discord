import requests

Headers = {"Content-Type":"application/json"}
proxyDict = { 
              "http"  : "127.0.0.1:80", 
              "https" : "127.0.0.1:80"
            }

Json = {"fingerprint":"", "email":"andanotherone1334@gmail.com", "username":"BotLol", "password":"CoolPassword", "invite":None, "consent":True, "gift_code_sku_id":None, "captcha_key":""}
Token = requests.post("https://discordapp.com/api/v6/auth/register",headers=Headers ,json=Json, proxies=proxyDict)
print(Token.content)
