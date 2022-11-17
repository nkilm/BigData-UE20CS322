#!/usr/bin/env python3
import sys
import json

for line in sys.stdin:
    word = line.strip()
    try:
	    obj = json.loads(word)
	    if obj['location']>1700 and obj['location']<2500 and obj['sensor_id']<5000 and obj['pressure']>=93500.00 and obj['humidity']>=72.00 and obj['temperature']>=12.00:
	    	print(f"{obj['timestamp']},1")
    except Exception as e:
    	continue