from getNewReport import currentCotReport
from analyzeReport import averages, changes, matches
from variables import traderPositions
from promptUser import getMinimumPercentFilter


def applyPercentFilter(m, position, percentMinimum):
    # Returns true if the percent change meets or exceeds percent minimum

    x = float(getattr(changes[m], position))

    if (x >= percentMinimum) or (x <= -percentMinimum):
        return True

    return False


def printReport(position, percentMinimum):
    # Iterate through the existing matches (current positioning & average positioning)
    # Print out a report with the percent change using the selected minimum as the filter

    def printOut(m, position):
        reportDate = currentCotReport[m].date
        assetTitle = currentCotReport[m].title
        currentNum = getattr(currentCotReport[m], position)
        averageNum = getattr(averages[m], position)
        changePercent = getattr(changes[m], position)

        print(reportDate)
        print(assetTitle)
        print(position)
        print('current: ', currentNum)
        print('average: ', averageNum)
        print('change: ', changePercent, '%')
        print()

    for match in matches:
        if (applyPercentFilter(match, position, percentMinimum)):
            printOut(match, position)


def runProgram():
    percentMinimum = getMinimumPercentFilter()

    for position in traderPositions:
        printReport(position, percentMinimum)


runProgram()
