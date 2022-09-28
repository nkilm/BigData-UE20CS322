#!/usr/bin/env python3

import sys

""" 
Mapper for Task 1 

Team ID: BD1_616_659_661_667

"""

for line in sys.stdin:

    # preprocessing step - ignore lines starting with "#"
    if(line.startswith("#")):
        continue
    
    # remove whitespace
    line = line.strip()
    src, dest = line.split()

    try:
        src = int(src)
        dest = int(dest)
    except ValueError:
        continue

    try:
        print("%d\t%d" % (src, dest))
    except Exception:
        continue
        # print(e)