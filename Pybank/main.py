import os
import csv
PyBankcsv = os.path.join('c:/Users/rtmcl/Documents/GitHub/python-challenge/Pybank','Resources','budget_data.csv')
#with open(PyBankcsv, 'r') as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")
    #csv_header = next(csvreader) 

# Open and read csv
#with open(Pybankcsv, newline="") as csvfile:
 #   csvreader = csv.reader(csvfile, delimiter=",")
#NumMonths = sum(1 for row in csvreader)
#print(NumMonths) 
# Read in the CSV file

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

      
    #for row in csvreader:
        #print(row)

#emply lists for month and revenue data
months = []
revenue = []


for row in csvread:
months.append(row[0])
revenue.append(int(row[1]))

#find total months
total_months = len(months)
