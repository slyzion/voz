#!/usr/bin/python3

from voz_lib import voz_datetime


class Tools:
    def __init__(self, option):
        self.option = option.lower()

    def exec(self):
        if self.option == '&time;':
            return voz_datetime.getTime()
        elif self.option == '&date;':
            return voz_datetime.getDate()

