import threading, discord, asyncio

_UserId = 1
_TokenFile = "C:\\Tokens.txt"
_Message = ""

class TokenThread(threading.Thread):
    def __init__(self, Token):
        threading.Thread.__init__(self)
        self.Token = Token
        return
    
    def run(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        Token = self.Token
        Bot = discord.Client()

        print("Starting..")

        try:
            async def status_task():
                Person = await Bot.fetch_user(_UserId)
                while True:
                    await Person.send(_Message)
                    print("Sent Message")
                    await asyncio.sleep(.5)

            @Bot.event
            async def on_ready():
                await Bot.change_presence(status=discord.Status.offline)

                Bot.loop.create_task(status_task())
            print("Running bot")
            Bot.run(Token, bot=False)
        except:
            print("False Token")



for Token in open(_TokenFile):
    TokenThread(Token=Token.replace("\n", "")).start()
    time.sleep(.5)
