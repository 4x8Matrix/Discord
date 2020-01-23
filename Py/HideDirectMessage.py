import threading, discord, asyncio

_PlayerId = 1
_Token = ""

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
                Person = await Bot.fetch_user(_PlayerId)
                for DM in Bot.private_channels:
                    if DM.__class__ == discord.DMChannel:
                        if DM.recipient == Person:
                            print("Located DM channel.")
                            async for message in DM.history(limit=5000):
                                if message.author == Bot.user:
                                    print("Hidden: Lol")
                                    await message.edit(content="𒐫"*1500)
                    else:
                        pass

                print("Finished!")

            @Bot.event
            async def on_ready():
                Bot.loop.create_task(status_task())

            Bot.run(Token, bot=False)
        except:
            print("False Token")

TokenThread(Token=_Token).start()
