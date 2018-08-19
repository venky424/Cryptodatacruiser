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

for key,value in dataresult.items():
	datanew=dataresult[key]
	datanew["Asset"]=key
	
output.writerow(datanew.keys())

for key,value in dataresult.items():
	datanew=dataresult[key]
	datanew["Asset"]=key
	output.writerow(datanew.values())	
