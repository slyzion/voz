#!/usr/bin/python3

import tools

import json
import random
try:
    from playsound import playsound
    from gtts import gTTS
except:
    print("Biblioteca de reprodução de voz não está instalada")

obj = ""
with open('datasets/chat_dataset_pt.json', 'r') as file:
    data = file.read()
    obj = json.loads(data)
    file.close()

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
    
    if resp[0] == '&':
        tool = tools.Tools(resp)
        resp = tool.exec()
    
    print(resp)
    try:
        #print(1)
        filename = "voice.mp3"
        #print(2)
        tts = gTTS(resp, lang='pt', slow=False)
        #print(3)
        tts.save(filename)
        playsound(filename)
        #print(4)
    except Exception as e:
        print(e)

    if text == "sair":
        exit(0)