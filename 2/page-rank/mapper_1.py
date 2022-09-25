#!/usr/bin/env python3

import sys

""" Mapper for Task 1 """

for line in sys.stdin:

    # preprocessing step - ignore lines starting with "#"
    if(line.startswith("#")):
        continue

    # remove whitespace
    line = line.strip()
    src, dest = line.split("\t")

    try:
        print("%s\t%s" % (src, dest))
    except Exception:
        continue
        # print(e)
