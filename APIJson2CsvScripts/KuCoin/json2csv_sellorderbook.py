import json
import csv
import sys

inputFile=sys.argv[1]
outputFile=sys.argv[2]

inputFile=open(inputFile,"r", encoding='utf8')
outputFile=open(outputFile,'w', newline='', encoding='utf8')

data=json.load(inputFile)
dataresult=data["data"]
timestamp=data["timestamp"]

inputFile.close()

output=csv.writer(outputFile,delimiter=';')

output.writerow((['Rate','Quantity','Total','Market','Timestamp']))

for row in dataresult:
	row.append("KCS-BTC")
	row.append(timestamp)
	output.writerow(row)