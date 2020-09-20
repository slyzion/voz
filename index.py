#!/usr/bin/python3

import tools        # voz tools

import string
import unidecode
import json
import random
import os
import re

try:
    from playsound import playsound     # play audios
    from gtts import gTTS               # get voice from google
except:
    print("> Instale primeiro as dependencias!!!")
    exit(0)

###### get 'config.json' functionalities
with open() as file:
    sys_append = 


while True:
    os.system('./bin/syncKeywords')
    ######## - Entrada - ########
    # get text
    print(">", end=" ")
    text = input()
    #############################

    ######## - Processamento do texto - ########
    # clean text
    text = unidecode.unidecode(text)                        # remove accentuation
    table = str.maketrans(dict.fromkeys(string.punctuation))# remove punctuation signals
    for i in table:
        text = text.replace(chr(i), ' ')                    # remove punctuation signals
    text = re.sub(' +', ' ', text).strip()                  # remove extra spaces
    text = text.lower()                                     # text to lower case
    text = text.split(" ")                                  # split text

    ############################################

    ######## - Processamento da resposta - ########
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

    #print(keys)

    # get chat answers
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
        #print(count)
        if count > 1:
            text = i['answer']
            for k in text:
                resp.append(k)

    #print("resp>",resp)

    # escolher qual a resposta a dar
    if not resp:
        resp = str(random.choice(["Não consigo perceber", "Não percebi", "OK", "Fixe"]))
    else:
        resp = str(random.choice(resp))


    # se resposta comecar com '&' executa comando correspondente
    cmd = ""
    if resp[0] == '&':
        tool = tools.Tools(resp)
        resp, cmd = tool.exec()

    # print response
    print(resp)
    try:
        #print(1)
        filename = "voice.wav"
        #print(2)
        tts = gTTS(resp, lang='pt', slow=False)
        #print(3)
        tts.save(filename)
        playsound(filename)
        #print(4)
        os.remove(filename)
    except Exception as e:
        print(e)

    if cmd == '&sair;':
        exit(0)