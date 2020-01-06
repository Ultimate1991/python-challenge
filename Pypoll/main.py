import os
import csv

csvpath = Pypollcsv = os.path.join('c:/Users/rtmcl/Documents/GitHub/python-challenge/Pypoll','Resources','election_data.csv')

#variables
total_votes = 0
candidates_unique = []
candidate_vote_count = []

with open(election_data.csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #Total votes cast
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




