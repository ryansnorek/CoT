# --------------------------------------------------------------------------------
# Gets current CFTC weekly report >> Futures-Only Commitments of Traders
# Loads report into dictionary object 'currentCotReport'
# --------------------------------------------------------------------------------
from urllib.request import urlretrieve as retrieve
import csv


class CotData:
    def __init__(self, title, date, openInterest,
                 dealerLong, dealerShort,
                 assetManLong, assetManShort,
                 levMoneyLong, levMoneyShort
                 ):
        self.title = title
        self.date = date
        self.openInterest = openInterest
        self.dealerLong = dealerLong
        self.dealerShort = dealerShort
        self.assetManLong = assetManLong
        self.assetManShort = assetManShort
        self.levMoneyLong = levMoneyLong
        self.levMoneyShort = levMoneyShort


def loadReportData():
    CoT_fin_url = 'https://www.cftc.gov/dea/newcot/FinFutWk.txt'
    retrieve(CoT_fin_url, 'cotFin.txt')
    cotReport = {}

    # Read through the data and store each section into an array
    with open('cotFin.txt', 'r') as textFile:
        for line in textFile:
            data = str(line.splitlines()).split(',')
            title = data[0].replace('"', '').replace('[', '').replace("'", '')
            date = data[2]
            openInterest = data[7].replace(' ', '')
            dealerLong = data[8].replace(' ', '')
            dealerShort = data[9].replace(' ', '')
            assetManLong = data[11].replace(' ', '')
            assetManShort = data[12].replace(' ', '')
            levMoneyLong = data[14].replace(' ', '')
            levMoneyShort = data[15].replace(' ', '')

            # Load object with variables
            cotReport[title] = CotData(
                title, date, openInterest,
                dealerLong, dealerShort,
                assetManLong, assetManShort,
                levMoneyLong, levMoneyShort
            )
    return cotReport


currentCotReport = loadReportData()
