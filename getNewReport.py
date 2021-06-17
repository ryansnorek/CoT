# --------------------------------------------------------------------------------
# Gets current CFTC weekly report >> Futures-Only Commitments of Traders
# Loads report into dictionary object 'currentCotReport'
# --------------------------------------------------------------------------------
from urllib.request import urlretrieve as retrieve
import csv


class CotData:
    def __init__(self, title, date, openInterest,
                 assetManLong, assetManShort,
                 levMoneyLong, levMoneyShort,
                 openInterestWeekChange,
                 assetManLongWeekChange,
                 assetManShortWeekChange,
                 levMoneyLongWeekChange,
                 levMoneyShortWeekChange
                 ):
        self.title = title
        self.date = date
        self.openInterest = openInterest
        self.assetManLong = assetManLong
        self.assetManShort = assetManShort
        self.levMoneyLong = levMoneyLong
        self.levMoneyShort = levMoneyShort
        self.openInterestWeekChange = openInterestWeekChange
        self.assetManLongWeekChange = assetManLongWeekChange
        self.assetManShortWeekChange = assetManShortWeekChange
        self.levMoneyLongWeekChange = levMoneyLongWeekChange
        self.levMoneyShortWeekChange = levMoneyShortWeekChange


def loadReportData():
    CoT_fin_url = 'https://www.cftc.gov/dea/newcot/FinFutWk.txt'
    retrieve(CoT_fin_url, 'cotFin.txt')
    cotReport = {}

    # Read through the data and store each section into an array
    # Remove spaces and clean up text
    with open('cotFin.txt', 'r') as textFile:
        for line in textFile:
            data = str(line.splitlines()).split(',')
            title = data[0].replace('"', '').replace('[', '').replace("'", '')
            date = data[2]
            openInterest = data[7].replace(' ', '')
            assetManLong = data[11].replace(' ', '')
            assetManShort = data[12].replace(' ', '')
            levMoneyLong = data[14].replace(' ', '')
            levMoneyShort = data[15].replace(' ', '')
            openInterestWeekChange = data[24].replace(' ', '')
            assetManLongWeekChange = data[28].replace(' ', '')
            assetManShortWeekChange = data[29].replace(' ', '')
            levMoneyLongWeekChange = data[31].replace(' ', '')
            levMoneyShortWeekChange = data[32].replace(' ', '')

            # Load object with data variables
            cotReport[title] = CotData(
                title, date, openInterest,
                assetManLong, assetManShort,
                levMoneyLong, levMoneyShort,
                openInterestWeekChange,
                assetManLongWeekChange,
                assetManShortWeekChange,
                levMoneyLongWeekChange,
                levMoneyShortWeekChange
            )
    return cotReport


currentCotReport = loadReportData()
