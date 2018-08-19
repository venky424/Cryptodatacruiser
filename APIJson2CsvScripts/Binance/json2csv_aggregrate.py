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

header=(['Aggregrate TradeID','Price','Quantity','First TradeID','Last TradeID','Timestamp','WasBuyerMarker','WasTradePriceBestMatch','Symbol'])

output.writerow(header)

for row in data:
	row["Symbol"]='BNBBTC'
	output.writerow(row.values())	