#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if line[5] == "question":
        #get id
        node = line[0]
        length = len(line[4])
        writer.writerow([node, 'A', length])

    elif line[5] == "answer":
        node = line[6]
        length = len(line[4])
        writer.writerow([node, 'B', length])



        

