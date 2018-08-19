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

header=(['Symbol','Id','Last','LowestAsk','HighestBid','PercentChange','BaseVolume','QouteVolume','isFrozen','High24Hr','Low24Hr'])

output.writerow(header)

for key,value in data.items():
	datakey=data[key]
	row=([key,datakey["id"],datakey["last"],datakey["lowestAsk"],datakey["highestBid"],datakey["percentChange"],datakey["baseVolume"],datakey["quoteVolume"],datakey["isFrozen"],datakey["high24hr"],datakey["low24hr"]])
	output.writerow(row)	