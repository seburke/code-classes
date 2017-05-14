#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re

regex = '([(\d\.)]+) (.*) (.*) \[(.*?)\] "(.*?)" (\d+) (.*)'


for line in sys.stdin:
    match = re.match(regex, line.strip())
    if match:
    	data = match.groups()
    	url = data[4].split(' ')[1]
    	urlFormatted = url.replace('http://www.the-associates.co.uk', '')
    	print urlFormatted
