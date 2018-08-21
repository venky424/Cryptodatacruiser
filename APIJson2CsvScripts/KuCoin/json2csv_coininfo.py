import json
import csv
import sys

inputFile=sys.argv[1]
outputFile=sys.argv[2]

inputFile=open(inputFile,"r")
outputFile=open(outputFile,'w', newline='')

data=json.load(inputFile)
dataresult=data["data"]

inputFile.close()

output=csv.writer(outputFile)

output.writerow(dataresult.keys())
output.writerow(dataresult.values())
	