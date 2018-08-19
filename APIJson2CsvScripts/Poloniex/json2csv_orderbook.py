import json
import csv
import sys


fileInput = sys.argv[1]
fileOutput = sys.argv[2]
              

inputFile = open(fileInput,"r")
outputFile = open (fileOutput,'w',newline='')
data= json.load(inputFile)
dataasks=data["asks"]
databids=data["bids"]
isfrozen=data["isFrozen"]
seq=data["seq"]
inputFile.close()


for row in dataasks:
	dataasksnew=row
	dataasksnew.append("asks")
	dataasksnew.append('BTC')
	dataasksnew.append(isfrozen)
	dataasksnew.append(seq)
	
for row in databids:
	databidsnew=row
	databidsnew.append("bids")
	databidsnew.append('BTC')
	databidsnew.append(isfrozen)
	databidsnew.append(seq)

header=(['Quantity','Rate','Type','Symbol','isFrozen','Seq'])

output =csv.writer(outputFile)
output.writerow(header)
           

for row in dataasks:
	output.writerow(row)

 

for row in databids:
	output.writerow(row)

 

