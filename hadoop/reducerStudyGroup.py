#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys



currentNodeKey = None
currentNodeStudents = []

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    thisKey, student = data_mapped

    if currentNodeKey and currentNodeKey != thisKey:
        print currentNodeKey, '\t', currentNodeStudents
        currentNodeKey = thisKey
        currentNodeStudents = []

    currentNodeKey = thisKey
    currentNodeStudents.append(student)

if currentNodeKey != None:
    print currentNodeKey, '\t', currentNodeStudents
