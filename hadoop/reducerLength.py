#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys



currentNodeKey = None
questionLength = 0
totalLength = 0
totalAnswers = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    thisKey, source, length = data_mapped

    if source == '"A"':
        if currentNodeKey:
            avg = 0
            if totalAnswers > 0:
                avg = totalLength / float(totalAnswers)
            print currentNodeKey, '\t', questionLength, '\t', avg

        currentNodeKey = thisKey
        questionLength = length
        totalLength = 0
        totalAnswers = 0

    elif currentNodeKey == thisKey:
        totalLength += int(length.replace('"', ''))
        totalAnswers += 1

if currentNodeKey:
    avg = 0
    if totalAnswers > 0:
        avg = totalLength / float(totalAnswers)
    print currentNodeKey, '\t', questionLength, '\t', avg