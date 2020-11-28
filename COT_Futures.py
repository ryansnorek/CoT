from urllib.request import urlretrieve as retrieve
CoT_fin_url = 'https://www.cftc.gov/dea/newcot/FinFutWk.txt'
CoT_dis_url = 'https://www.cftc.gov/dea/newcot/f_disagg.txt'

# Skeletons for lists
CoT_list = []
title, date, open_interest = [], [], []
am_long, am_long_change = [], []
am_short, am_short_change = [], []
am_spreading, am_spreading_change = [], []
lf_long, lf_short, lf_spreading = [], [], []
lf_long_change, lf_short_change, lf_spreading_change = [], [], []

def financials():
    # Retrieve CoT Financial Futures from URL
    retrieve(CoT_fin_url,'cot_fin.txt')

    # Open CoT Financial Futures file and organize data
    with open("cot_fin.txt", 'r') as txtFile:
        organize_data(txtFile)

def disaggregated():
    # Retrieve CoT Disaggregated Futures from URL
    retrieve(CoT_dis_url,'cot_dis.txt')

    # Open CoT Disaggregated Futures file and organize data
    with open("cot_dis.txt", 'r') as txtFile:
        organize_data(txtFile)

def organize_data(txtFile):
    for line in txtFile:
        # Add each section to the CoT List
        stripped_line = line.strip()
        CoT_list.append(stripped_line)

    # Loop through the CoT List and isolate each item by comma 
    for line in CoT_list:
        line = line.split(',') 

        # Skip lines that have a comma in the main title (unsolved solution)
        if len(line[0]) > 12:
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

    # Print a numbered list of title selections
    i = 0
    for selection in title:
        print(i, title[i])
        i += 1

    # Get input from user and format data 
    print("-------------------------")
    inp = int(input("Type a number from the list or hit enter to quit program: "))
    while inp != '':
        print(title[inp])
        print("-------------------------")
        print("Date:",date[inp])
        print("Open Interest:",open_interest[inp])
        print("-------------------------")
        print("Asset Managers / Institutions")
        
        print("\nLong:",am_long[inp],am_long_change[inp],"change")
        print("Short:",am_short[inp],am_short_change[inp],"change")
        print("Spreading:",am_spreading[inp],am_spreading_change[inp],"change")
        print("-------------------------")
        print("Leveraged Funds")
        
        print("\nLong:",lf_long[inp],lf_long_change[inp],"change")
        print("Short:",lf_short[inp],lf_short_change[inp],"change")
        print("Spreading:",lf_spreading[inp],lf_spreading_change[inp],"change")
        print("-------------------------")
        inp = int(input("Type a number from the list or hit enter to quit program: "))


# Starting Menu
print("1. Financials")
print("2. Disaggregated")

# Ask user to select a CoT report
select_report = int(input("Select a CoT futures report to view "))
if select_report == 1:
    financials()
elif select_report == 2:
    disaggregated()


            

        


        

        
            
   

        
           
            

       
           
          
            
       
            
       

       

        
    
    
    
   





            

        


        

        
            
   

        
           
            

       
           
          
            
       
            
       

       

        
    
    
    
   


