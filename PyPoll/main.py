#!/usr/bin/env python
# coding: utf-8

#import os provides function for interacting with the operating system(OS)
#import csv is a module for importing and reading csv files
import os
import csv

#provides the path of the csv file "election_data.csv"
election_data = os.path.join("Resources","election_data.csv")


#initially setting variables
vote_count = 0
candidate_percent = 0

#created lists to store data
candidate_khan= []
candidate_correy = []
candidate_li = []
candidate_otooley = []
winner = []

#opens up the csvfile from the data_budget path provided above
#csvreader iterates over each line of the csvfile
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #next(csvreader) just reads over the header; removing it from calculations
    csv_header = next(csvreader)
    
    #going through each row after the header and first_row
    for row in csvreader:
        
        #using a count to grab total votes
        vote_count += 1
        
        #using a conditional to sort the candidates for calculations
        #then storing that data to a list for each candidate
        if (row[2] == "Khan"):
            candidate_khan.append(row[2])
        elif (row[2]) == "Correy":
            candidate_correy.append(row[2])
        elif (row[2]) == "Li":
            candidate_li.append(row[2])
        elif (row[2]) == "O'Tooley":
            candidate_otooley.append(row[2])
            
        #Finding out number of votes for each candidate
        khan_votes = len(candidate_khan)
        correy_votes = len(candidate_correy)
        li_votes = len(candidate_li)
        otooley_votes = len(candidate_otooley)
        
        #Finding out percent of votes for each candidate
        khan_per = (khan_votes/vote_count) *100
        correy_per = (correy_votes/vote_count) *100
        li_per = (li_votes/vote_count) *100
        otooley_per = (otooley_votes/vote_count) *100
        
        #Setting up to compare each candidate list to find the winner
        #the max value will be the winner
        winner = [khan_votes,correy_votes,li_votes,otooley_votes]
        final_winner = max(winner)
        
        #Using a conditional to find the max value and who has that max value
        if final_winner == khan_votes:
            winner_name = 'Khan'
        elif final_winner == correy_votes:
            winner_name = "Correy"
        elif final_winner == li_votes:
            winner_name = "Li"
        elif final_winner == otooley_votes:
            winner_name = "O'Tooley"

#created a string to be able to call on for both print and output
results = (

            f"Election Results\n"
            f"-----------------------------\n"
            f"Total Votes:{vote_count}\n"
            f"-----------------------------\n"
            f"Kahn:{ckhan} {khan_per:.3f}% ({khan_votes})\n"
            f"Correy: {correy_per:.3f}% ({correy_votes})\n"
            f"Li: {li_per:.3f}% ({li_votes})\n"
            f"O'Tooley: {otooley_per:.3f}% ({otooley_votes})\n"
            f"-----------------------------\n"
            f"Winner:{winner_name}\n"
            f"-----------------------------\n"
            )



#print results
print(results)


#provides path of output results for new text file analysis.txt
outpath = os.path.join("Analysis", "analysis.txt")


#opens file for writing and writes the results to analysis.txt
with open(outpath, "w") as text_file:
    text_file.write(results)


