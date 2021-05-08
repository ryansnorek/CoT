from getNewReport import currentCotReport
from analyzeReport import averages, changes, matches
from variables import classProperties


def applyPercentFilter(index, classProperty, percentRange):
    x = float(getattr(changes[index], classProperty))
    if (x > percentRange) or (x < -percentRange):
        return True
    else:
        return False


def printReport(classProperty, percentRange):
    for i in matches:
        if (applyPercentFilter(i, classProperty, percentRange)):
            print(currentCotReport[i].title)
            print(classProperty)
            print('current: ', getattr(currentCotReport[i], classProperty))
            print('average: ', getattr(averages[i], classProperty))
            print('change: ', getattr(changes[i], classProperty), '%')

# Adjust number for minimum percent change to check for, 50 = 50%, 100 = 100%, etc
for p in classProperties:
    printReport(p, 100)
