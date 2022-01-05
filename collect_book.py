import json
import csv

bookfile = r'C:\Users\base\Documents\Endeavours\Crypt\ir\IRbooklog\20200409_irbook.csv'
outfile = r'C:\Users\base\Documents\Endeavours\Crypt\ir\IRbooklog\20200409_pricediff.csv'
sizeThreshold = 0.1

outs = []
with open(bookfile) as f:
    lines = f.readlines()
    for line in lines:
        k = json.loads(line)
        t = k['startTime']
        bidSum = 0
        askSum = 0
        bidPrice = k['Bids'][9][0]
        askPrice = k['Asks'][9][0]
        for i in range(10):
            bidSum += k['Bids'][i][1]
            if bidSum > sizeThreshold:
                bidPrice = k['Bids'][i][0]
                break
        for i in range(10):
            askSum += k['Asks'][i][1]
            if askSum > sizeThreshold:
                askPrice = k['Asks'][i][0]
                break
        bitstampRef = k['BitstampRef']
        outs.append([t, bidPrice, askPrice, bitstampRef])

with open(outfile, 'w', newline='') as g:
    writer = csv.writer(g, dialect='excel')
    writer.writerows(outs)
