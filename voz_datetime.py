#!/usr/bin/python3

import json
#import ntplib

def getTime():
   import time
   """ntp = ntplib.NTPClient()
   ntpResponse = ntp.request('europe.pool.ntp.org', version=3)

   if (ntpResponse):
      print(time.ctime(ntpResponse.tx_time))
   """
   t = time.localtime()
   current_time = time.strftime("%H:%M", t)
   return "São "+current_time


def getDate():
   import datetime
   d = datetime.datetime.now()
   current_day = d.strftime("%d de ")
   current_year = d.strftime(" de %Y")
   current_month = int(d.strftime("%m"))

   obj = ""
   with open('lang/months_pt.json') as file:
      data = file.read()
      obj = json.loads(data)
      file.close()

   for i in obj:
      if i['number'] == current_month:
         return "Hoje é "+current_day+i['name']+current_year

if __name__ == "__main__":
   print(getDate())