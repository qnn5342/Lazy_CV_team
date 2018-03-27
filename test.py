#!/usr/bin/python3
import sys
import csv

inpFile = open(sys.argv[1], newline='', encoding='utf-8')
csvReader = csv.reader(inpFile, delimiter=',', quotechar='"')

outpFile = open(sys.argv[2], mode='w', encoding='utf-8')

for row in csvReader:
	for field in row:
		try:
			float(field)
			print(field, end = ',', file = outpFile)
		except ValueError:
			print('"' + str(field).replace('\n', '').replace('"', '""') + '"', end = ',', file = outpFile)
	print('', file = outpFil)
