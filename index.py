#!/usr/bin/python3

import json
import random
try:
    from gtts import gTTS
    from io import BytesIO
except:
    print("Biblioteca de reprodução de voz não está instalada, executa no cmd: pip install pyttsx3")

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
        mp3_fp = BytesIO()
        print(2)
        tts = gTTS(resp, lang='en')
        print(3)
        tts.write_to_fp(mp3_fp)
        print(4)

        # engine = pyttsx3.init()
        # engine.setProperty('volume', 0.4)
        # engine.setProperty('rate', 125)
        # engine.setProperty('voice', 'english')
        # engine.say(resp)
        # engine.runAndWait()
    except ExceptError as e:
        print(e)
