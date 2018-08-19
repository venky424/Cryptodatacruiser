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

header=(['Open Time','Open','High','Low','Close','Volume','Close Time','Qoute Asset Volume','No Of Trades','Taker Base Asset Volume','Take Qoute Asset Volume','Ignore','Symbol'])

output.writerow(header)

for row in data:
	row.append('ETHBTC')
	output.writerow(row)
	