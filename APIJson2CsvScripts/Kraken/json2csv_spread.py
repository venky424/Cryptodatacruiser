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

lastupdatedid=dataresult["last"]
dataKey=dataresult["BCHEUR"]

header=(['Time','Bid','Ask','PairName','LastUpdatedId'])

output.writerow(header)

for row in dataKey:
	row.append('BCHEUR')
	row.append(lastupdatedid)
	output.writerow(row)
	
