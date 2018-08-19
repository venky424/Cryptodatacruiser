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

totalbtc=data["totalBTC"]
totaleth=data["totalETH"]
totalusdt=data["totalUSDT"]
totalxmr=data["totalXMR"]
totalxusd=data["totalXUSD"]
output.writerow(['Market','Symbol1','Symbol1_Price','Symbol2','Symbol2_Price','TotalBTC','TotalETH','TotalUSDT','TotalXMR','TotalXUSD'])

for key,value in data.items():
	datanew=data[key]
	if type(datanew) is dict:
		row=[key,list(datanew.keys())[0],list(datanew.values())[0],list(datanew.keys())[1],list(datanew.values())[1]]
		row.append(totalbtc)
		row.append(totaleth)
		row.append(totalusdt)
		row.append(totalxmr)
		row.append(totalxusd)
		output.writerow(row)