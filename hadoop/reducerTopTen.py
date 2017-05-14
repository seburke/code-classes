#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

currentTag = None
tagNum = 0
topTenTags = []

for line in sys.stdin:
    tag = line.strip()

    if currentTag and currentTag != tag:
        topTenTags.append((currentTag, tagNum))
        if len(topTenTags) >= 10:
            #sort 
            topTenTags.sort(key=lambda x: x[1])
            #trim
            topTenTags = topTenTags[-10:]

        currentTag = tag
        tagNum = 0



    currentTag = tag
    tagNum += 1


if currentTag != None:
    topTenTags.append((currentTag, tagNum))
    if len(topTenTags) >= 10:
        #sort 
        topTenTags.sort(key=lambda x: x[1])
        #trim
        topTenTags = topTenTags[-10:]

topTenTags.reverse()
for t in topTenTags:
    print t[0], '\t', t[1]

