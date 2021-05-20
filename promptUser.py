# --------------------------------------------------------------------------------
# Prompt user to select parameters for analysis on current CoT report
# --------------------------------------------------------------------------------
from variables import cotYearDB


def getMinimumPercentFilter():

    def prompt():
        minimumPercentFilter = int(
            input("Select a minimum percent change filter for CoT report: "))

        if (minimumPercentFilter < 0):
            getMinimumPercentFilter()

        return minimumPercentFilter

    return prompt()


def selectDatabase():

    for year in cotYearDB:
        print(cotYearDB[year])

    def prompt():
        database = input("Type which database to compare averages from: ")

        for year in cotYearDB:
            if (database == cotYearDB[year]):
                return database

    return prompt()
