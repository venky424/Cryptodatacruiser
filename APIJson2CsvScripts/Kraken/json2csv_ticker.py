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

dataKey=dataresult["BCHEUR"]
dataa=dataKey["a"]
print(dataa)
print(type(dataa))
datab=dataKey["b"]
datac=dataKey["c"]
datav=dataKey["v"]
datap=dataKey["p"]
datat=dataKey["t"]
datal=dataKey["l"]
datah=dataKey["h"]
datao=dataKey["o"]


header=(['PairName','Ask_Price','Ask_Whole_Lot_Volume','Ask_Lot_Volume','Bid_Price','Bid_Whole_Lot_Volume','Bid_Lot_Volume','LastTradePrice','LastTradeLotVolume','TodayVolume','Last24hVolume','TodayVolumeWeightedAveragePrice','Last24hrWeightedAveragePrice','NoOfTradesToday','NoOfTradesLast24h','TodayLow','Last24hLow','TodayHigh','Last24hHigh','TodayOpeningPrice'])

row=(['BCHEUR',dataa[0],dataa[1],dataa[2],datab[0],datab[1],datab[2],datac[0],datac[1],datav[0],datav[1],datap[0],datap[1],datat[0],datat[1],datal[0],datal[1],datah[0],datah[1],datao])

output.writerow(header)
output.writerow(row)

