#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	body = line[4].strip()
	node = line[0]
	words = re.findall(r"[\w']+", body)
	for word in words: 
		print word.lower(), '\t', node

	