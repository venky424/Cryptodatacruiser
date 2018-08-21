import json
import csv
import sys

inputFile=sys.argv[1]
outputFile=sys.argv[2]

inputFile=open(inputFile,"r", encoding='utf8')
outputFile=open(outputFile,'w', newline='', encoding='utf8')

data=json.load(inputFile)
dataresult=data["data"]

inputFile.close()

output=csv.writer(outputFile,delimiter=';')

output.writerow(dataresult[0].keys())

for row in dataresult:
	output.writerow(row.values())