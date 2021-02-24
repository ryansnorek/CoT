from urllib.request import urlretrieve as retrieve
import csv

cotArray = []
cotReport = []
cotTitles = {}


class Instrument:
    def __init__(self, title, date, openInterest,
                 dealerLong, dealerShort,
                 assetManLong, assetManShort,
                 leveragedLong, leveragedShort
                 ):
        self.title = title
        self.date = date
        self.openInterest = openInterest
        self.dealerLong = dealerLong
        self.dealerShort = dealerShort
        self.assetManLong = assetManLong
        self.assetManShort = assetManShort
        self.leveragedLong = leveragedLong
        self.leveragedShort = leveragedShort


def getFinData():
    CoT_fin_url = 'https://www.cftc.gov/dea/newcot/FinFutWk.txt'
    retrieve(CoT_fin_url, 'cotFin.txt')

    # Read through the data and store each section into an array
    with open('cotFin.txt', 'r') as textFile:
        for line in textFile:
            x = line.splitlines()
            cotArray.append(x)

    for key, line in enumerate(cotArray):
        # Store an indexed list of titles for user selection
        findTitle = str(line).split('"')
        title = findTitle[1]
        cotTitles[key] = title

        # Create a report with the rest of the data
        data = str(line).split(',')
        date = data[2]
        openInterest = data[7]
        dealerLong = data[8]
        dealerShort = data[9]
        assetManLong = data[11]
        assetManShort = data[12]
        leveragedLong = data[14]
        leveragedShort = data[15]

        cotReport.append(Instrument(
            title, date, openInterest,
            dealerLong, dealerShort,
            assetManLong, assetManShort,
            leveragedLong, leveragedShort
        ))


def getSelectionFromUser():
    print('============================================')
    print('1. View CoT reports')
    print('2. View reports from favorites')
    print('============================================')
    selection = int(input('What would you like to do? '))
    if selection == 1:
        viewReport()
    if selection == 2:
        favs = pullFavorites()


def viewReport():
    # Display indexed titles and ask for user selection
    for key in cotTitles:
        print(key, cotTitles[key])

    selection = input('Enter selections separated by a comma. ')
    userSelection = selection.split(',')

    # Run the program for each selection
    for choice in userSelection:
        x = int(choice)
        printReport(x)

    # Save as favorites to new file
    askFavs = input('Save this list to favorites? (y/n)')
    if askFavs == 'y':
        print('List saved!')
        pushFavorites(userSelection)
    else:
        exit()


def pushFavorites(newFavs):
    # Creates new or overwrites existing file
    with open('favorites.text', 'w') as textFile:
        for fav in newFavs:
            textFile.write(fav + ' ')


def pullFavorites():
    with open('favorites.text', 'r') as textFile:
        favs = textFile.readlines()
    return favs


def printReport(x):
    print('============================================')
    print(cotReport[x].title)
    print(cotReport[x].date)
    print('Open Interest: ', cotReport[x].openInterest)
    print('\nBanks')
    print('Long: ', cotReport[x].dealerLong)
    print('Short: ', cotReport[x].dealerShort)
    print('\nAsset Managers')
    print('Long: ', cotReport[x].assetManLong)
    print('Short: ', cotReport[x].assetManShort)
    print('\nHedge Funds')
    print('Long: ', cotReport[x].leveragedLong)
    print('Short: ', cotReport[x].leveragedShort)
    print('============================================')


getFinData()
getSelectionFromUser()
