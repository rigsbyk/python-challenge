#import os provides function for interacting with the operating system(OS)
#import csv is a module for importing and reading csv files
import os
import csv

#provides the path of the csv file "election-data.csv"
election_data = os.path.join("Resources","election_data.csv")

#initially setting variables
vote_count = 0

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #next(csvreader) just reads over the header; removing it from calculations
    csv_header = next(csvreader)
    
    #going through each row after the header and first_row
    for row in csvreader:
               
        #using a count to grab total votes
        vote_count += 1
    
    print("Election Results")
    print("---------------")
    print("Total Votes: " + str(vote_count))
    print("---------------")
    print("Results")
    print("---------------")
    print("winner")
    print("---------------")