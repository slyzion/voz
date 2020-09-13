#!/usr/bin/python3

import voz_datetime as tm


class Tools:
    def __init__(self, option):
        self.option = option.lower()

    def exec(self):
        if self.option == '&time;':
            return tm.getTime()
        elif self.option == '&date;':
            return tm.getDate()

