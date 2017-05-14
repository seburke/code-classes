#!/usr/bin/python

import sys

oldKey = None
nodes = []
occurrences = 0
for line in sys.stdin:

    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, node = data_mapped

    if oldKey and oldKey != thisKey:
        nodes.sort()
        print oldKey, '\t', occurrences, '\t', ','.join([str(x) for x in nodes])
        oldKey = thisKey
        nodes = []
        occurrences = 0

    oldKey = thisKey
    occurrences += 1
    try:
        nodes.append(int(node))
    except: 
        pass

if oldKey != None:
    nodes.sort()
    print oldKey, '\t', occurrences, '\t', ','.join([str(x) for x in nodes])
    