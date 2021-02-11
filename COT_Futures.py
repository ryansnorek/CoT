from urllib.request import urlretrieve as retrieve
import csv
CoT_fin_url = 'https://www.cftc.gov/dea/newcot/FinFutWk.txt'
CoT_dis_url = 'https://www.cftc.gov/dea/newcot/f_disagg.txt'

# Skeletons for lists
CoT_list = []
CoT_shortList = []
title, date, open_interest = [],[],[]
# Asset Managers
am_long, am_long_change = [],[]
am_short, am_short_change = [],[]
# Hedge Funds
hf_long, hf_long_change = [],[]
hf_short, hf_short_change = [],[]
# Commercial Banks
cb_long, cb_long_change = [],[]
cb_short, cb_short_change = [],[]

def financialFutures():
    # Retrieve CoT Financials Futures text file from URL 
    retrieve(CoT_fin_url,'cot_fin.txt')

    # Open text file, organize data into a full list, and create short list
    with open("cot_fin.txt", 'r') as txtFile:
        organizeData(txtFile)

    CoT_shortList.extend([
        CoT_list[4], #Euro
        CoT_list[17], # S&P Energy
        CoT_list[18], # S&P 500
        CoT_list[19], # S&P Financial
        CoT_list[22], # Nasdaq
        CoT_list[24], # Russel
        CoT_list[28], # Emerging
        CoT_list[31], # Bonds
        CoT_list[33], # 2YR
        CoT_list[34], # 10YR
        CoT_list[42], # Bitcoin
        CoT_list[43], # DXY
        CoT_list[44] # Vix
    ])
    return CoT_shortList
def parseFinancialData(data):
    for line in data:
        line = line.split(',') 
        # Title, Date, Open Interest
        title.append(line[0]) 
        date.append(line[2])
        open_interest.append(line[7])

        # Commercial Banks
        cb_long.append(line[8])
        cb_long_change.append(line[25])
        cb_short.append(line[9])
        cb_short_change.append(line[26])
        # Asset Managers
        am_long.append(line[11])
        am_long_change.append(line[28])
        am_short.append(line[12])
        am_short_change.append(line[29])
        # Hedge Funds
        hf_long.append(line[14])
        hf_long_change.append(line[31])
        hf_short.append(line[15])
        hf_short_change.append(line[32])
def printFinancialReport():
    for i in range(len(CoT_shortList)):
        print("\n--------------------------------------------------")
        print(title[i])
        print("--------------------------------------------------")
        print("Date:",date[i])
        print("Open Interest:",open_interest[i])
        print("--------------------------------------------------")
        print("Commercial Banks")
        print("Long:",cb_long[i],cb_long_change[i],"change")
        print("Short:",cb_short[i],cb_short_change[i],"change")
        print("--------------------------------------------------")
        print("Asset Managers")
        print("Long:",am_long[i],am_long_change[i],"change")
        print("Short:",am_short[i],am_short_change[i],"change")
        print("--------------------------------------------------")
        print("Hedge Funds")
        print("Long:",hf_long[i],hf_long_change[i],"change")
        print("Short:",hf_short[i],hf_short_change[i],"change")

def disaggregatedFutures():
    # Retrieve CoT Disaggregated Futures from URL
    retrieve(CoT_dis_url,'cot_dis.txt')

    # Open text file, organize data into a full list, and create short list
    with open("cot_dis.txt", 'r') as txtFile:
        organizeData(txtFile)

    CoT_shortList.extend([
        CoT_list[64], # Natural Gas
        CoT_list[178], # WTI
        CoT_list[185], # Platinum
        CoT_list[188], # Silver
        CoT_list[189], # Copper
        CoT_list[190], # Gold
        CoT_list[191] # Gasoline
    ])
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
            # Hedge Funds / Swap Dealers
            hf_long.append(line[11])
            hf_long_change.append(line[59])
            hf_short.append(line[12])
            hf_short_change.append(line[60])
            # Asset Managers
            am_long.append(line[14])
            am_long_change.append(line[62])
            am_short.append(line[15])
            am_short_change.append(line[63])

        if len(line[0]) > 12:
            # Title, Date, Open Interest
            title.append(line[0]) 
            date.append(line[2])
            open_interest.append(line[7])
            # Hedge Funds / Swap Dealers
            hf_long.append(line[10])
            hf_long_change.append(line[58])
            hf_short.append(line[11])
            hf_short_change.append(line[59])
            # Asset Managers
            am_long.append(line[13])
            am_long_change.append(line[61])
            am_short.append(line[14])
            am_short_change.append(line[62])
def printDisaggregatedReport():
    for i in range(len(CoT_shortList)):
        print("\n--------------------------------------------------")
        print(title[i])
        print("--------------------------------------------------")
        print("Date:",date[i])
        print("Open Interest:",open_interest[i])
        print("--------------------------------------------------")
        print("Hedge Funds / Swap Dealers")
        print("Long:",hf_long[i],hf_long_change[i],"change")
        print("Short:",hf_short[i],hf_short_change[i],"change")
        print("--------------------------------------------------")
        print("Asset Managers")
        print("Long:",am_long[i],am_long_change[i],"change")
        print("Short:",am_short[i],am_short_change[i],"change")

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

