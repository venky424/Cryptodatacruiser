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

LastUpdatedId=dataresult["last"]
dataKey=dataresult["BCHEUR"]

header=(['Time','Open','High','Low','Close','VWAP','Volume','Count','LastUpdatedId','PairName'])

output.writerow(header)

for row in dataKey:
	row.append(LastUpdatedId)
	row.append('BCHEUR')
	output.writerow(row)
	
