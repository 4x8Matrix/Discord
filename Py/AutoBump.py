import threading, discord, asyncio, time

ChannelID_List = [1, 2]
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
                while True:
                    for ChannelID in ChannelID_List:
                        try:
                            Channel = Bot.get_channel(ChannelID)
                            await Channel.send("!d bump")
                            print(f"{Channel.guild.name} has been bumped.")
                        except Exception as e:
                            print(e)
                    time.sleep(5405)

                print("Finished!")

            @Bot.event
            async def on_ready():
                Bot.loop.create_task(status_task())

            Bot.run(Token, bot=False)
        except:
            print("False Token")

TokenThread(Token=_Token).start()
