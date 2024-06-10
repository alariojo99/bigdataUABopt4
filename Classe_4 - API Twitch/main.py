from twitchAPI.twitch import Twitch
import json
import time

public = "j0vk1o0choelmhc6jg7jc3lzjbhak2"
secret = ""

twitch = Twitch(public, secret)

next = None

loop = 0

def get_str(next, loop):
    resposta = twitch.get_streams(language="es", after=next, first=100)
    print(len(resposta["data"]))
    with open(f"{loop}.json", 'w', encoding='utf-8') as f:
        json.dump(resposta, f, ensure_ascii=False, indent=4)

    try:
        next = resposta["pagination"]["cursor"]
        print("hi ha nova pàgina")
        loop += 1
        time.sleep(2)
        get_str(next, loop)
    except:
        print("final")
        pass



get_str(next, loop)