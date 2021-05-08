# --------------------------------------------------------------------------------
# Stores all variables...
# --------------------------------------------------------------------------------

classProperties = [
    'openInterest',
    'dealerLong', 'dealerShort',
    'assetManLong', 'assetManShort',
    'levMoneyLong', 'levMoneyShort'
]

title = []
openInterest = []
dealerLong = []
dealerShort = []
assetManLong = []
assetManShort = []
levMoneyLong = []
levMoneyShort = []
totalLong = []
totalShort = []
otherLong = []
otherShort = []

cotData = [
    title, openInterest,
    dealerLong, dealerShort,
    assetManLong, assetManShort,
    levMoneyLong, levMoneyShort,
    totalLong, totalShort,
    otherLong, otherShort
]


# cotAverages = []


# Label: DB table of CoT report by year
cotYearDB = {
    'cot2020': 'cotreports2020',
    'cot2019': 'cotreports2019',
    'cot2018': 'cotreports2018',
    'cot2017': 'cotreports2017',
    'cot2016': 'cotreports2016',
    'cot2015': 'cotreports2015'
}
