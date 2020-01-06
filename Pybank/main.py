import os
import csv
PyBankcsv = os.path.join("Resources","budget_data.csv")
# Open and read csv
#with open(Pybankcsv, newline="") as csvfile:
 #   csvreader = csv.reader(csvfile, delimiter=",")
#NumMonths = sum(1 for row in csvreader)
#print(NumMonths) 
# Read in the CSV file

with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)