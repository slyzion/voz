#!/usr/bin/python3

from modules import voz_datetime


class Tools:
    def __init__(self, text):
        self.text = text

    def exec(self):
        red = True
        self.option = ""
        for i in self.text:
            if i == ';':
                red = False
                self.option += ';'
            if i != ';' and red == True:
                self.option += i
        
        #print(self.option)
        self.text = self.text.replace(self.option, "")

        if self.option == '&sair;':
            return self.text, self.option
        if self.option == '&time;':
            return voz_datetime.getTime(), None
        elif self.option == '&date;':
            return voz_datetime.getDate(), None

