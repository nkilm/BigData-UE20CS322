#!/usr/bin/env python3

"""
Consumer for Task 2
Team ID: BD1_616_659_661_667
"""
import json
import sys
from collections import OrderedDict

from kafka import KafkaConsumer

if len(sys.argv) < 2:
    print("Topic not provided")
    sys.exit(1)

KAFKA_TOPIC = sys.argv[1]
consumer = KafkaConsumer(KAFKA_TOPIC)

avg_crop_prices = {}

for msg in consumer:
    line = msg.value.decode("utf-8")

    if line == "EOF":
        # When EOF is reached the dictionary avg_crop_prices will contain all information
        for state, prices in avg_crop_prices.items():
            # Taking average of prices
            prices["Min"] = round(sum(prices["Min"]) / len(prices["Min"]), 2)
            prices["Max"] = round(sum(prices["Max"]) / len(prices["Max"]), 2)

        print(json.dumps(OrderedDict(sorted(avg_crop_prices.items()))))
        sys.exit(0)

    info = line.split(",")
    state, min_p, max_p = info[0], info[-3], info[-2]

    try:
        min_p = float(min_p)
        max_p = float(max_p)
    except TypeError as e:
        continue

    try:
        if avg_crop_prices.get(state) is None:
            avg_crop_prices[state] = {}
            avg_crop_prices[state]["Min"] = [min_p]
            avg_crop_prices[state]["Max"] = [max_p]
        else:
            # print(avg_crop_prices[state])
            avg_crop_prices[state]["Min"].append(min_p)
            avg_crop_prices[state]["Max"].append(max_p)
    except:
        continue
