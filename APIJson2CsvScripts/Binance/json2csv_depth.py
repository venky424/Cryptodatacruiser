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

dataBid=data["bids"]

dataLastUpdatedId=data["lastUpdateId"]

header=(['Bids_Price','Bids_Quantity','Ignore','LastUpdatedId','Symbol'])

output.writerow(header)

for row in dataBid:
	row.append(dataLastUpdatedId)
	row.append('BNBBTC')
	output.writerow(row)