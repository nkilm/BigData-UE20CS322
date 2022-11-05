#!/usr/bin/env python3

"""
Producer for Task 2
Team ID: BD1_616_659_661_667
"""
import sys

from kafka import KafkaProducer

if len(sys.argv) < 2:
    print("Topic not provided")
    sys.exit(1)

KAFKA_TOPIC = sys.argv[1]

producer = KafkaProducer()

for line in sys.stdin:
    try:
        line = line.strip()
        producer.send(KAFKA_TOPIC, line.encode("utf-8"))

        # send as soon as the message is sent, maintains order
        producer.flush()
    except:
        continue
