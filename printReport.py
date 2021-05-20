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

    for m in matches:
        if (applyPercentFilter(m, position, percentMinimum)):
            print(currentCotReport[m].date)
            print(currentCotReport[m].title)
            print(position)
            print('current: ', getattr(currentCotReport[m], position))
            print('average: ', getattr(averages[m], position))
            print('change: ', getattr(changes[m], position), '%')
            print()


def runProgram():
    percentMinimum = getMinimumPercentFilter()

    for position in traderPositions:
        printReport(position, percentMinimum)


runProgram()
