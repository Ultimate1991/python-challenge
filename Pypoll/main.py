import os
import csv

# path to data file
budget_data_csv = os.path.join('election_data.csv')

#variables
total_votes = 0
candidates_unique = []
candidate_vote_count = []

with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #This is the total votes cast, just count rows
        total_votes += 1
        #read in the candidate from column 3 of csv
        candidate_in = (row[2])
        #if candidate alreaady in list then locate the candidate by index # and increment the vote count by 1
        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            #if candidate was not found in candidates_unique list then append to list and add 1 to vote count
            candidates_unique.append(candidate_in)
            candidate_vote_count.append(1)


#import os
#import csv

#PyPollcsv = os.path.join,'Resources','election_data.csv')
#Variables
#total_votes = 0
#candidates_unique = []
#candidate_vote_count = []

#read the csv file
#with open(election_data, newline="") as csvfile:
    #csvreader = csv.reader(csvfile, delimiter=",")
    #csv_header = next(csvreader)

    #for row in csvreader:
        #This is the total votes cast, just count rows
        #total_votes += 1
        #read in the candidate from column 3 of csv
        #candidate_in = (row[2])
        #if candidate alreaady in list then locate the candidate by index # and increment the vote count by 1
        #if candidate_in in candidates_unique:
            #candidate_index = candidates_unique.index(candidate_in)
            #candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        #else:
            #if candidate was not found in candidates_unique list then append to list and add 1 to vote count
            #candidates_unique.append(candidate_in)
            #candidate_vote_count.append(1)

