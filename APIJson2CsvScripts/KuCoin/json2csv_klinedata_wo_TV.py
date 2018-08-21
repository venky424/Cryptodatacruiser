import json
import csv
import sys

inputFile=sys.argv[1]
outputFile=sys.argv[2]

inputFile=open(inputFile,"r", encoding='utf8')
outputFile=open(outputFile,'w', newline='', encoding='utf8')

data=json.load(inputFile)
dataresult=data["data"]


for rowres in dataresult:
	dataresultnew=rowres
	dataresultnew.append("ETH-BTC")

inputFile.close()

output=csv.writer(outputFile,delimiter=';')

output.writerow((['Timestamp','Open','High','Low','Close','Amount','Miscellaneous','Market']))

for row in dataresult:
	output.writerow(row)
	