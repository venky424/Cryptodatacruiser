import json
import csv
import sys

inputFile=sys.argv[1]
outputFile=sys.argv[2]

inputFile=open(inputFile,"r")
outputFile=open(outputFile,'w', newline='')
data=json.load(inputFile)
dataresult=data["result"]

inputFile.close()

output=csv.writer(outputFile)

output.writerow(dataresult[0].keys())

for row in dataresult:
	output.writerow(row.values())
	