import json
import csv
import sys

inputFile=sys.argv[1]
outputFile=sys.argv[2]

inputFile=open(inputFile,"r", encoding='utf8')
outputFile=open(outputFile,'w', newline='', encoding='utf8')

data=json.load(inputFile)
dataresult=data["data"]



inputFile.close()

output=csv.writer(outputFile,delimiter=';')

output.writerow((['Deal_Timestamp','Deal_Price','CoinPair']))

for row in dataresult:
	coinpair=row["coinPair"]
	datadeals=row["deals"]
	for rowdeal in datadeals:
		rowdeal.append(coinpair)
		output.writerow(rowdeal)