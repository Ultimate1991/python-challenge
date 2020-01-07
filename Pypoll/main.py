import os
import csv

csvpath = Pypollcsv = os.path.join('c:/Users/rtmcl/Documents/GitHub/python-challenge/Pypoll','Resources','election_data.csv')

# Open and read the CSV
with open(csvpath, newline="") as csvfile:
    #print(csvreader)
    
    # Read header row
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    
 
    #Declare variables
    Candidates = {}
    Count = 0
    Votes_Cast = 0
    percent_of_votes = 0
    Most_Votes = 0
    Most_Voted = ""
    

    
    for row in csvreader:
        
        # Count the total number of votes cast
        candidate = row[2]
        Count += 1
        if candidate in Candidates.keys():
            Candidates[candidate] += 1
        else:
            Candidates[candidate] = 1
       
    
    
    # Print Statements
    print("Election Results")
    print("-------------------------------")
    print(f"Total Votes: {Count}")
    print("-------------------------------")
    
            
    #total number of votes
    for candidate in Candidates:
        Votes_Cast += Candidates[candidate]
    
        # percent of votes
        percent_of_votes = (Candidates[candidate])/(Count) * 100
        print(f"{candidate}: {int(percent_of_votes)}% {Votes_Cast}")
        
        if Candidates[candidate] > Most_Votes:
            Most_Voted = candidate
            Most_Votes = Candidates[candidate]
        
        
    
    # The winner of the election based on popular vote.
    print("-------------------------------")
    
    print(f"Winner: {Most_Voted}")
    
    print("-------------------------------")



