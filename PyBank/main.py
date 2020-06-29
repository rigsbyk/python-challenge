
#import os provides function for interacting with the operating system(OS)
#import csv is a module for importing and reading csv files
import os
import csv

#provides the path of the csv file "budget-data.csv"
data_budget = os.path.join("Resources","budget-data.csv")

net_total = 0
total_months = 0 

#using the data_budget path, open the file; using alias csvfile
#csvreader iterates over each line of the csvfile using the comma as a field separator(delimiter)
with open(data_budget) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #next(csvreader) just reads over the header; removing it from calculations
    csv_header = next(csvreader)

    #going through each row after the header and first_row
    for row in csvreader:
    	print(row)

    	#using a count to get total number of rows 
        total_months += 1
        
        #using a counter to total up Profit/Losses
        net_total += int(row[1])



    print("Total Months:" + str(total_months))
    print("Total:" + str(net_total))
    print("Average Change:")
    print("Greatest Increase in Profit:")
    print("Greatest Decrease in Profit:")

       # file1.write("Hello \n")

#provides path of output results for new text file analysis.txt
outpath = os.path.join("Analysis","analysis.txt")

#opens file for writing and writes the results to analysis.txt
with open(outpath, "w") as text_file:
	
	text_file.write("Financial Analysis\n")
	text_file.write("------------------------\n")
	text_file.write("Total Months: " + str(total_months) + "\n")
	text_file.write("Total: " + str(net_total) + "\n")
	text_file.write("Average Change:\n")
	text_file.write("Greatest Increase in Profits:\n")
	text_file.write("Greatest Decrease in Profits:\n")






