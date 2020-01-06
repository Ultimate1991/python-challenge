import os
import csv


PyBankcsv = os.path.join('c:/Users/rtmcl/Documents/GitHub/python-challenge/Pybank','Resources','budget_data.csv')



#Create Lists
profit = []
monthly_changes = []
date = []

#Variables
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

      
    for row in csvreader:
        print(row)
            # Conducting the ask
    for row in csvreader:    
      # Use count to count the number months in this dataset
      count = count + 1 

      # Will need it when collecting the greatest increase and decrease in profits
      date.append(row[0])



