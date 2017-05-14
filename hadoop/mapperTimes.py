#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import csv
import re
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	try: 
		dateString = line[8].split('.')[0]
		hour = datetime.strptime(dateString, "%Y-%m-%d %H:%M:%S").hour
		author = line[3]
		print author, '\t', hour
	except: 
		pass