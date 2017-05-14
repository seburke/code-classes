#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

def reducer():

    currentUser = None
    currentUserKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")

        thisKey = data_mapped[0]
        source = data_mapped[1]

        if source == '"A"':
            currentUser = data_mapped[2:]
            currentUserKey = thisKey
        elif currentUserKey == thisKey:
            newLine = [thisKey] + data_mapped[2:] + currentUser
            print '\t'.join(newLine)

reducer()

