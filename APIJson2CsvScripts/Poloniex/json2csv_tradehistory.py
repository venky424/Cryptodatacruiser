import json
import csv
import sys

inputFile=sys.argv[1]
outputFile=sys.argv[2]

inputFile=open(inputFile,"r")
outputFile=open(outputFile,'w', newline='')
data=json.load(inputFile)

inputFile.close()

for row in data:
	datanew=row
	datanew['Symbol']='BTC_NXT'

output=csv.writer(outputFile)

output.writerow(data[0].keys())

for row in data:
	output.writerow(row.values())
	