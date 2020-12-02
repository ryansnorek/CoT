from urllib.request import urlretrieve as retrieve
CoT_fin_url = 'https://www.cftc.gov/dea/newcot/FinFutWk.txt'
CoT_dis_url = 'https://www.cftc.gov/dea/newcot/f_disagg.txt'

# Skeletons for lists
CoT_list = []
CoT_shortList = []
title, date, open_interest = [], [], []
am_long, am_long_change = [], []
am_short, am_short_change = [], []
am_spreading, am_spreading_change = [], []
lf_long, lf_short, lf_spreading = [], [], []
lf_long_change, lf_short_change, lf_spreading_change = [], [], []

def financialFutures():
    # Retrieve CoT Financials Futures text file from URL 
    retrieve(CoT_fin_url,'cot_fin.txt')

    # Open text file, organize data into a full list, and create short list
    with open("cot_fin.txt", 'r') as txtFile:
        organizeData(txtFile)

    CoT_shortList.append(CoT_list[4]) # Euro
    CoT_shortList.append(CoT_list[18]) # S&P Energy
    CoT_shortList.append(CoT_list[19]) # S&P 500
    CoT_shortList.append(CoT_list[20]) # S&P Financial
    CoT_shortList.append(CoT_list[25]) # Nasdaq
    CoT_shortList.append(CoT_list[27]) # Russel
    CoT_shortList.append(CoT_list[32]) # Emerging
    CoT_shortList.append(CoT_list[35]) # Bonds
    CoT_shortList.append(CoT_list[37]) # 2YR
    CoT_shortList.append(CoT_list[38]) # 10YR
    CoT_shortList.append(CoT_list[46]) # Bitcoin
    CoT_shortList.append(CoT_list[47]) # DXY
    CoT_shortList.append(CoT_list[48]) # Vix
    return CoT_shortList
def parseFinancialData(data):
    for line in data:
        line = line.split(',') 
        # Title, Date, Open Interest
        title.append(line[0]) 
        date.append(line[2])
        open_interest.append(line[7])

        # Asset Managers / Institutions
        am_long.append(line[11])
        am_long_change.append(line[28])
        am_short.append(line[12])
        am_short_change.append(line[29])
        am_spreading.append(line[13])   
        am_spreading_change.append(line[30])

        # Leveraged Funds
        lf_long.append(line[14])
        lf_long_change.append(line[31])
        lf_short.append(line[15])
        lf_short_change.append(line[32])
        lf_spreading.append(line[16])
        lf_spreading_change.append(line[33])
def printFinancialReport():
    for i in range(len(CoT_shortList)):
        print("\n--------------------------------------------------")
        print(title[i])
        print("--------------------------------------------------")
        print("Date:",date[i])
        print("Open Interest:",open_interest[i])
        print("--------------------------------------------------")
        print("Asset Managers / Institutions")

        print("\nLong:",am_long[i],am_long_change[i],"change")
        print("Short:",am_short[i],am_short_change[i],"change")
        print("Spreading:",am_spreading[i],am_spreading_change[i],"change")
        print("--------------------------------------------------")
        print("Leveraged Funds")

        print("\nLong:",lf_long[i],lf_long_change[i],"change")
        print("Short:",lf_short[i],lf_short_change[i],"change")
        print("Spreading:",lf_spreading[i],lf_spreading_change[i],"change")

def disaggregatedFutures():
    # Retrieve CoT Disaggregated Futures from URL
    retrieve(CoT_dis_url,'cot_dis.txt')

    # Open text file, organize data into a full list, and create short list
    with open("cot_dis.txt", 'r') as txtFile:
        organizeData(txtFile)

    CoT_shortList.append(CoT_list[75]) # Natural Gas
    CoT_shortList.append(CoT_list[193]) # WTI
    CoT_shortList.append(CoT_list[201]) # Platinum
    CoT_shortList.append(CoT_list[204]) # Silver
    CoT_shortList.append(CoT_list[205]) # Copper
    CoT_shortList.append(CoT_list[206]) # Gold
    CoT_shortList.append(CoT_list[207]) # Gasoline
    return CoT_shortList
def parseDisaggregatedData(data):
    for line in data:
        line = line.split(',')

        # WTI Crude Oil title has 2 commas, shift over by 1
        if len(line[0]) < 12:
            # Title, Date, Open Interest
            title.append(line[0]) 
            date.append(line[3])
            open_interest.append(line[8])

            # Leveraged Funds / Swap Dealers
            lf_long.append(line[11])
            lf_long_change.append(line[59])
            lf_short.append(line[12])
            lf_short_change.append(line[60])
            lf_spreading.append(line[13])
            lf_spreading_change.append(line[61])

            # Asset Managers / Institutions
            am_long.append(line[14])
            am_long_change.append(line[62])
            am_short.append(line[15])
            am_short_change.append(line[63])
            am_spreading.append(line[16])   
            am_spreading_change.append(line[64])

        if len(line[0]) > 12:
            # Title, Date, Open Interest
            title.append(line[0]) 
            date.append(line[2])
            open_interest.append(line[7])

            # Leveraged Funds / Swap Dealers
            lf_long.append(line[10])
            lf_long_change.append(line[58])
            lf_short.append(line[11])
            lf_short_change.append(line[59])
            lf_spreading.append(line[12])
            lf_spreading_change.append(line[60])

            # Asset Managers / Institutions
            am_long.append(line[13])
            am_long_change.append(line[61])
            am_short.append(line[14])
            am_short_change.append(line[62])
            am_spreading.append(line[15])   
            am_spreading_change.append(line[63])
def printDisaggregatedReport():
    for i in range(len(CoT_shortList)):
        print("\n--------------------------------------------------")
        print(title[i])
        print("--------------------------------------------------")
        print("Date:",date[i])
        print("Open Interest:",open_interest[i])
        print("--------------------------------------------------")
        print("Leveraged Funds / Swap Dealers")

        print("\nLong:",lf_long[i],lf_long_change[i],"change")
        print("Short:",lf_short[i],lf_short_change[i],"change")
        print("Spreading:",lf_spreading[i],lf_spreading_change[i],"change")
        print("--------------------------------------------------")
        print("Asset Managers / Institutions")

        print("\nLong:",am_long[i],am_long_change[i],"change")
        print("Short:",am_short[i],am_short_change[i],"change")
        print("Spreading:",am_spreading[i],am_spreading_change[i],"change")

# Organize the data from the CoT text file into a full list
def organizeData(data):
    for line in data:
        stripped_line = line.strip()
        CoT_list.append(stripped_line)
    return CoT_list

# Get selection from user to process CoT data and print report
def runProgram():
    print('\n1. Financial Futures')
    print('2. Disaggregated Futures')
    selection = int(input("\nChoose category: "))
    if selection == 1:
        parseFinancialData(financialFutures())
        printFinancialReport()
    elif selection == 2:
        parseDisaggregatedData(disaggregatedFutures())
        printDisaggregatedReport()

runProgram()
