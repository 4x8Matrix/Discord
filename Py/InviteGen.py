import random, proxy, requests, time, json
API = "https://discordapp.com/api/invite/"
Character = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}

while True:
    invite = API+"".join([str(Char) for Char in random.sample(Character, 6)])
    print(invite+"\n")
    Recv = requests.get(invite).content
    Data = json.loads(str(Recv)[2:][:-1])
    try:
        print(Data["guild"]["name"])
        print(invite)
    except:
        print("False Invite")
    
    time.sleep(5)
