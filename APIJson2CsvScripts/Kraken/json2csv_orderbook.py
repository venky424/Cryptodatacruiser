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

dataKey=dataresult["BCHEUR"]
dataasks=dataKey["asks"]
databids=dataKey["bids"]

header=(['Price','Volume','TimeStamp','Type','PairName'])

output.writerow(header)

for row in dataasks:
	row.append('ASK')
	row.append('BCHEUR')
	output.writerow(row)
	
for row in databids:
	row.append('BID')
	row.append('BCHEUR')
	output.writerow(row)