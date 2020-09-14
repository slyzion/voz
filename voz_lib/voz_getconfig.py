#!/usr/bin/python3

import json

class Config:
    def __init__(self, filepath):
        self.configfile = filepath

    def getlang(self):
        obj = ""
        with open(self.configfile, 'r') as file:
            data = file.read()
            obj = json.loads(data)
    
        return obj['lang']

if __name__ == "__main__":
    config = Config()
    print(config.getlang())