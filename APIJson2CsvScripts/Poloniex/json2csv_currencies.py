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

header=(['Symbol','Id','Name','TxFee','MinConf','DepositAddress','Disabled','Delisted','Frozen'])

output.writerow(header)

for key,value in data.items():
	datakey=data[key]
	row=([key,datakey["id"],datakey["name"],datakey["txFee"],datakey["minConf"],datakey["depositAddress"],datakey["disabled"],datakey["delisted"],datakey["frozen"]])
	output.writerow(row)	