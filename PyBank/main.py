#import os provides function for interacting with the operating system(OS)
#import csv is a module for importing and reading csv files
import os
import csv


#provides the path of the csv file "budget-data.csv"
data_budget = os.path.join("Resources","budget-data.csv")


#initially setting the variables changes
changes = 0
net_total = 0
previous = 0
total_months = 0 

#created lists to store data
date = [] 
profits = []


#opens up the csvfile from the data_budget path provided above
#csvreader iterates over each line of the csvfile
with open(data_budget) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #next(csvreader) just reads over the header; removing it from calculations
    csv_header = next(csvreader)
    
    #next(csvreader) on the first row so that it can calculate the Average Change
    #starting with the second row of calcuable data
    first_row = next(csvreader)
    previous = int(first_row[1])
    net_total = net_total + int(first_row[1])
    total_months = total_months + 1
    
    #going through each row after the header and first_row
    for row in csvreader:
        
        #using a count to get total number of rows for total months count
        total_months += 1
        
        #using a counter to total up Profit/Losses
        net_total = net_total + int(row[1])
     
        #as it goes through for row in csvreader, it calculates the changes
        #Then it adds those calculations to the profit list
        changes = int(row[1]) - previous
        profits.append(changes)
        previous = int(row[1])
        
        #calculating greatest increase/decrease of profits using stored profits data
        greatestincrease = max(profits)
        greatestdecrease = min(profits)
        
        #grabbing the associated date of greatest increase/decrease using the index list method
        date.append(row[0])
        idate = date[profits.index(greatestincrease)]
        ddate = date[profits.index(greatestdecrease)]
    
    
#after calculating above you find the average of those changes to find the Average Change       
average_change = round(sum(profits)/len(profits),2)

#created a string to be able to call on for both print and output
results = (
            f"Financial Analysis\n"
            f"---------------------\n"
            f"Total Months:{total_months}\n"
            f"Total:{net_total}\n"
            f"Average Change:{average_change}\n"
            f"Greatest Increase in Profits: {idate} ${greatestincrease}\n"
            f"Greatest Decrease in Profits: {ddate} ${greatestdecrease}\n"
            )

#print results
print(results)

#provides path of output results for new text file analysis.txt
outpath = os.path.join("Analysis","analysis.txt")

#opens file for writing and writes the results to analysis.txt
with open(outpath, "w") as text_file:
    text_file.write(results)
    