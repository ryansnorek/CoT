
# --------------------------------------------------------------------------------
#  Returns averages from historical CoT data
# --------------------------------------------------------------------------------

import psycopg2
from functools import reduce
import math
from cot_variables import *
from config import cur


cotAverages = []


def loadData(code, year):
    # Select block in DB by year and market code
    cur.execute(
        f"SELECT * FROM {year} WHERE CFTC_Contract_Market_Code='{code}'")
    rows = cur.fetchall()

    # Iterate through each row and load arrays
    for row in rows:
        openInterest.append(row[3])
        dealerLong.append(row[4])
        dealerShort.append(row[5])
        assetManLong.append(row[6])
        assetManShort.append(row[7])
        levMoneyLong.append(row[8])
        levMoneyShort.append(row[9])
        totalLong.append(row[10])
        totalShort.append(row[11])
        otherLong.append(row[12])
        otherShort.append(row[13])


def getAverage(array):
    print(array)
    return math.floor(reduce((lambda x, y: x + y), array)/len(array))


def loadAverages():
    # Iterate through each array in cotData, get average, and store in new array
    for array in cotData:
        print(getAverage(array))
        # cotAverages.append(getAverage(array))
        # Clean slate to process the next data set
        array.clear()


item = 'JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE'


def runProgram(item):
    # Iterate through each year in the cot report DB and get the market code for the input futures contract
    for year in cotYearDB:
        cur.execute(
            f"SELECT CFTC_Contract_Market_Code FROM {cotYearDB[year]} WHERE '{item}' LIKE '%' || Market_and_Exchange_Names ||'%'")
        marketCode = cur.fetchone()[0]
        # Load trader position data from database
        loadData(marketCode, cotYearDB[year])
        loadAverages()


runProgram(item)

print(cotAverages)
