# --------------------------------------------------------------------------------
# Analyzes current CoT report vs historical CoT data
# --------------------------------------------------------------------------------
from ConfigDB import cur
from getNewReport import currentCotReport
from variables import *
from promptUser import selectDatabase
import psycopg2
import math


class CotData:
    def __init__(self, title, openInterest,
                 assetManLong, assetManShort,
                 levMoneyLong, levMoneyShort
                 ):
        self.title = title
        self.openInterest = openInterest
        self.assetManLong = assetManLong
        self.assetManShort = assetManShort
        self.levMoneyLong = levMoneyLong
        self.levMoneyShort = levMoneyShort


table = selectDatabase()


def loadAveragesFromDB():
    # Returns a dict object that contains the average positioning in CoT Report history

    cur.execute(
        f"SELECT * FROM {table}")
    DB = cur.fetchall()
    cotAverages = {}

    for item in DB:
        title = item[0]
        openInterest = item[3]
        assetManLong = item[6]
        assetManShort = item[7]
        levMoneyLong = item[8]
        levMoneyShort = item[9]

        cotAverages[title] = CotData(
            title, openInterest,
            assetManLong, assetManShort,
            levMoneyLong, levMoneyShort
        )

    return cotAverages


def findMatchingAverages():
    # Loads an array object with only the assets in the most
    # recent CoT Report that have comparable historical data.
    cotMatches = []

    for title in currentCotReport:
        cur.execute(
            f"SELECT EXISTS(SELECT 1 FROM {table} WHERE Market_and_Exchange_Names='{title}')")
        matchExists = cur.fetchone()[0]

        if (matchExists):
            cotMatches.append(title)

    return cotMatches


def getPercentChange():
    # Returns a dict object that contains the percent change between
    # the most recent CoT Report and the average

    def percentChange(x, y):
        # Returns the percent change between 2 inputs unless the input
        # is zero, in which case its a 100% change
        x, y = int(x), int(y)

        if (x == 0):
            return -100
        elif (y == 0):
            return 100

        return round(((x - y) / y * 100), 2)

    cotChange = {}
    tempStorage = []

    for title in matches:
        for el in traderPositions:
            current = getattr(currentCotReport[title], el)
            average = getattr(averages[title], el)
            tempStorage.append(percentChange(current, average))

        openInterest = tempStorage[0]
        assetManLong = tempStorage[1]
        assetManShort = tempStorage[2]
        levMoneyLong = tempStorage[3]
        levMoneyShort = tempStorage[4]

        cotChange[title] = CotData(
            title, openInterest,
            assetManLong, assetManShort,
            levMoneyLong, levMoneyShort
        )

        tempStorage.clear()

    return cotChange


averages = loadAveragesFromDB()
matches = findMatchingAverages()
changes = getPercentChange()
