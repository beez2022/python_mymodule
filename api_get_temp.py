# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 14:30:12 2022

@author: beekheng
"""

from urllib.request import urlopen
import json

def get_weather_pls(sID):
     sock = urlopen("https://api.data.gov.sg/v1//environment/air-temperature")
     result = sock.read()
     sock.close
     weather = json.loads(result)

     listof_temp = weather['items'][0]['readings']
     for info in listof_temp:
         if info['station_id'].lower() == sID.lower():
             return(info)
     return(False)
