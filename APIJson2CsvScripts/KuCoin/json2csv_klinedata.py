import json
import csv
import sys

inputFile=sys.argv[1]
outputFile=sys.argv[2]

inputFile=open(inputFile,"r", encoding='utf8')
outputFile=open(outputFile,'w', newline='', encoding='utf8')

data=json.load(inputFile)
datac=data["c"]
datat=data["t"]
datav=data["v"]
datah=data["h"]
datal=data["l"]
datao=data["o"]

kdlen=len(datac)

dataresult=[]

for i in range(kdlen):
	row=[datac[i],datat[i],datav[i],datah[i],datal[i],datao[i],'KCS-BTC']
	dataresult.append(row)
	

inputFile.close()

output=csv.writer(outputFile,delimiter=';')

output.writerow((['Close','Timestamp','Volume','High','Low','Open','Market']))

for row in dataresult:
	output.writerow(row)


	