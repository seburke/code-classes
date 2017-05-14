#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if line[5] == "question":
        #get id
        node = line[0]
        student = line[3]
        writer.writerow([node, student])

    elif line[5] != "node_type":
        node = line[7]
        student = line[3]
        writer.writerow([node, student])