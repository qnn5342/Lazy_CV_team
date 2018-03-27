#!/usr/bin/python3
import sys

inp_file = open(sys.argv[1], encoding="utf8" , mode='r')
for index, line in enumerate(inp_file):
	line = line.strip()
	fields =  line.split(",");
	match_id = str(fields[0])
#	if '"' == match_id:
#		print(line)
	try:
		int(match_id)
		print(match_id + ',', end = '')
	except ValueError:
		print('', end='')

# for line in sys.stdin:
# 	line = line.strip()
# 	fields =  line.split(",");
# 	timestamp = float(fields[0])
# 	ip = fields[1]
# 	value = datetime.datetime.fromtimestamp(timestamp)
# 	print(value.strftime('%Y-%m-%d') + "," + str(ip))
