#!/usr/bin/env python3
import sys
import json
from math import *

if(len(sys.argv)<3):
    print("Not all arguments provided.\nPlease enter Distance, Latitude and Longitude in order")
    exit(1)

D = float(sys.argv[1])
latitude = float(sys.argv[2])
longitude = float(sys.argv[3])

def getDistance(x1,y1,x2,y2):
    return int(sqrt((x2-x1)**2 + (y2-y1)**2))

for line in sys.stdin:
    word = line.strip()
    try:
        obj = json.loads(word)
        if obj['humidity']>48.00 and obj['humidity']<54.00 and obj['temperature']>20.00 and obj['temperature']<24.00 and getDistance(obj['lat'],obj['lon'],latitude,longitude)<=D:
            print(f"{obj['timestamp']},1")
    except Exception as e:
        continue