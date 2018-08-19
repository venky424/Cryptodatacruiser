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

for row in data:
	datanew=row
	datanew["Symbol"]="BNBBTC"

output.writerow(data[0].keys())

for row in data:
	output.writerow(row.values())
	