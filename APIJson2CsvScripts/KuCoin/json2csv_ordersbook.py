import json
import csv
import sys

inputFile=sys.argv[1]
outputFile=sys.argv[2]

inputFile=open(inputFile,"r", encoding='utf8')
outputFile=open(outputFile,'w', newline='', encoding='utf8')

data=json.load(inputFile)
dataresult=data["data"]
datasell=dataresult["SELL"]
databuy=dataresult["BUY"]
timestamp=data["timestamp"]

for rowbuy in databuy:
	databuynew=rowbuy
	databuynew.append("KCS-BTC")
	databuynew.append("BUY")
	databuynew.append(timestamp)

for rowsell in datasell:
	datasellnew=rowsell
	datasellnew.append("KCS-BTC")
	datasellnew.append("SELL")
	datasellnew.append(timestamp)

inputFile.close()

output=csv.writer(outputFile,delimiter=';')

output.writerow((['Rate','Quantity','Total','Market','Type','Timestamp']))

for row in databuy:
	output.writerow(row)
	
for row in datasell:
	output.writerow(row)