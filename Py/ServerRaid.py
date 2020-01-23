import threading, discord, asyncio, requests

_Message = "Nice\n@everyone"
_ChannelId = 1
_ServerInvite = "Au97yh"
_TokenFile = "C:\\Tokens.txt"

class TokenThread(threading.Thread):
    def __init__(self, Token):
        threading.Thread.__init__(self)
        self.Token = Token
        return
    
    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        Token = self.Token

        headers = {'Authorization': Token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'}
        requests.post("https://canary.discordapp.com/api/v6/invite/{}".format(_ServerInvite), headers=headers)#, proxies=proxies)
        Bot = discord.Client()

        try:
            async def status_task():
                try:
                    while True:
                        channel = Bot.get_channel(_ChannelId)
                        await channel.send(_Message)
                        await asyncio.sleep(1)
                except:
                    pass

            @Bot.event
            async def on_ready():
                await Bot.change_presence(status=discord.Status.offline)

                Bot.loop.create_task(status_task())

            Bot.run(Token, bot=False)
        except:
            print("False Token")



for Token in open(_TokenFile):
    TokenThread(Token=Token.replace("\n", "")).start()
    time.sleep(.5)
