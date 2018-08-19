import json
import csv
import sys


fileInput = sys.argv[1]
fileOutput = sys.argv[2]
              

inputFile = open(fileInput,"r")
outputFile = open (fileOutput,'w',newline='')
data= json.load(inputFile)
dataoffers=data["offers"]
datademands=data["demands"]
inputFile.close()


for row in dataoffers:
	dataoffersnew=row
	dataoffersnew["Type"]="Offers"
	dataoffersnew["Symbol"]='BTC'
	
for row in datademands:
	datademandsnew=row
	datademandsnew["Type"]="Demands"
	datademandsnew["Symbol"]='BTC'


output =csv.writer(outputFile)
output.writerow(dataoffers[0].keys())
           

for row in dataoffers:
	output.writerow(row.values())

 

for row in datademands:
	output.writerow(row.values())

 

