import json
import csv
import sys


fileInput = sys.argv[1]
fileOutput = sys.argv[2]
              

inputFile = open(fileInput,"r")
outputFile = open (fileOutput,'w',newline='')
data= json.load(inputFile)
dataresult=data["result"]
databuy=dataresult["buy"]
datasell=dataresult["sell"]
inputFile.close()


for row in databuy:
	databuynew=row
	databuynew["Type"]="BUY"
	databuynew["Market"]='BTC-LTC'
	
for row in datasell:
	datasellnew=row
	datasellnew["Type"]="SELL"
	datasellnew["Market"]='BTC-LTC'

print (databuy[0])
print (datasell[0])

output =csv.writer(outputFile)
output.writerow(databuy[0].keys())
           

for row in databuy:
	output.writerow(row.values())

 

for row in datasell:
	output.writerow(row.values())

 

