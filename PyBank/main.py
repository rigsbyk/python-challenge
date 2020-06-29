
#import os provides function for interacting with the operating system(OS)
#import csv is a module for importing and reading csv files
import os
import csv

#provides the path of the csv file "budget-data.csv"
data_budget = os.path.join("Resources","budget-data.csv")

#using the data_budget path, open the file; using alias csvfile
#csvreader iterates over each line of the csvfile using the comma as a field separator(delimiter)
with open(data_budget) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #going through each row after the header and first_row
    for row in csvreader:
    	print(row)