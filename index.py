#!/usr/bin/python3

# Importacao de bibliotecas privadas
from voz_lib import voz_getconfig as getconf
import tools                            # execucao de comandos do utilizador 

# Importacao de bibliotecas publicas
import os
import json                             # acesso a ficheiros JSON
import random
try:
    from playsound import playsound     # tocar audios
    from gtts import gTTS               # obter audio voz do google
except:
    print("Biblioteca de reprodução de voz não está instalada")



# obtem a lingua das configuracoes
config = getconf.Config('src/config.json')
lang = config.getlang()


# Obtem as perguntas e respostas do ficheiro json
obj = ""
with open('src/'+lang+'/chat_dataset.json', 'r') as file:
    data = file.read()
    obj = json.loads(data)
    file.close()


# inicio do chat com a Voz
while True:
    # obter text do utilizador
    print(">", end=" ")
    text = input().strip().lower()

    # obter resposta para o utilizador
    lista = []
    for i in obj:
        if i["question"] == text:
            lista.append(str(i["answer"]))

    # escolher qual a resposta a dar
    resp = ""
    if not lista:
        resp = "Não consigo responder"
    else:
        resp = str(random.choice(lista))
    
    # se resposta comecar com '&' executa comando correspondente
    if resp[0] == '&':
        tool = tools.Tools(resp)
        resp = tool.exec()
    

    # TTS da resposta
    print(resp)
    try:
        #print(1)
        filename = "voice.mp3"
        #print(2)
        tts = gTTS(resp, lang=lang, slow=False)
        #print(3)
        tts.save(filename)
        playsound(filename)
        #print(4)
        os.remove(filename)
    except Exception as e:
        print(e)

    if text == "sair":
        exit(0)