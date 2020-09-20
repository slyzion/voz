#!/usr/bin/python3

import tools

import string
import unidecode
import json
import random
import os

try:
    from playsound import playsound     # tocar audios
    from gtts import gTTS               # obter audio voz do google
except:
    print("> Instale primeiro as dependencias!!!")
    exit(0)


while True:
    print(">", end=" ")
    text = input()

    # remove accentuation
    text = unidecode.unidecode(text)

    # remove punctuation signals
    table = str.maketrans(dict.fromkeys(string.punctuation))
    text= text.translate(table)

    # text to lower case
    text = text.lower()

    # split text
    text = text.split(" ")

    print(text)


    # get list of keywords
    obj = ""
    with open('src/keywords.json', 'r') as file:
        data = file.read()
        obj = json.loads(data)
        file.close()


    # get keywords from text
    keys = []
    for i in obj:
        for j in text:
            if i == j:
                keys.append(str(i))

    print(keys)

    ##################################
    with open('src/test.json', 'r') as file:
        data = file.read()
        obj = json.loads(data)
        file.close()

    # get answers for keywords
    resp = []
    for i in obj:
        count = 0               # initialize counter
        lista = i['keywords']   # get keywords for each answer
        for j in keys:
            for k in lista:
                if k == j:
                    count += 1     
        print(count)
        if count > 1:
            resp.append(i['answer'])


    # escolher qual a resposta a dar
    if not resp:
        resp = str(random.choice(["Não consigo perceber", "OK", "?", "\U0001F609"]))
    else:
        resp = str(random.choice(resp))

    

    # se resposta comecar com '&' executa comando correspondente
    if resp[0] == '&':
        tool = tools.Tools(resp)
        resp = tool.exec()

    # print response
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
        os.remove(filename)
    except Exception as e:
        print(e)


    if resp == "sair":
        exit(0)
