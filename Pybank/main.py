import os
import csv

# Set path for file
csvpath = PyBankcsv = os.path.join('c:/Users/rtmcl/Documents/GitHub/python-challenge/Pybank','Resources','budget_data.csv')

#print(csvpath)

# Open and read the CSV
with open(csvpath, newline="") as csvfile:
    #print(csvreader)
    
    # Read header row, print it, set it aside
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
 
    # Declare variables as empty lists
    Months = []
    Profit_Loss = []
    Differences = []
    Greatest_Increase_Date = ""
    Greatest_Decrease_Date = ""
    
    # Count total number of months the data encapsulates
    for row in csvreader:
        Months.append(row[0])   
        Profit_Loss.append(int(row[1]))
      
    
    # Print Statements
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months: ", len(Months))
    print("Net Total: $", sum(Profit_Loss))


 