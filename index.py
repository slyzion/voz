#!/usr/bin/python3

import json
import random
try:
    from playsound import playsound
    from gtts import gTTS
except:
    print("Biblioteca de reprodução de voz não está instalada")

with open('datasets/chat_dataset.json', 'r') as file:
    data = file.read()


obj = json.loads(data)

while True:
    print(">", end=" ")
    text = input().strip().lower()

    lista = []
    for i in obj:
        if i["question"] == text:
            lista.append(str(i["answer"]))

    resp = ""
    if not lista:
        resp = "Não consigo responder"
    else:
        # print(lista)
        resp = str(random.choice(lista))
    
    print(resp)
    try:
        print(1)
        filename = "voice.mp3"
        print(2)
        tts = gTTS(resp, lang='en', slow=False)
        print(3)
        tts.save(filename)
        playsound(filename)
        print(4)

        # engine = pyttsx3.init()
        # engine.setProperty('volume', 0.4)
        # engine.setProperty('rate', 125)
        # engine.setProperty('voice', 'english')
        # engine.say(resp)
        # engine.runAndWait()
    except Exception as e:
        print(e)
