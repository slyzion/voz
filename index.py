#!/usr/bin/python3

import json
import random
import pyttsx3

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

    engine = pyttsx3.init()
    engine.setProperty('volume', 0.4)
    engine.setProperty('rate', 125)
    engine.setProperty('voice', 'english')
    engine.say(resp)
    engine.runAndWait()
