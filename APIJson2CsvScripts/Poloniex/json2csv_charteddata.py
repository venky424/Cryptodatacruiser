import json
import csv
import sys

inputFile=sys.argv[1]
outputFile=sys.argv[2]

inputFile=open(inputFile,"r")
outputFile=open(outputFile,'w', newline='')
data=json.load(inputFile)
inputFile.close()

output=csv.writer(outputFile)

header=([list(data[0].keys())[0],list(data[0].keys())[1],list(data[0].keys())[2],list(data[0].keys())[3],list(data[0].keys())[4],list(data[0].keys())[5],list(data[0].keys())[6],list(data[0].keys())[7],'Symbol'])
output.writerow(header)

for row in data:
	row["Symbol"]='BTC_XMR'
	output.writerow(row.values())
	