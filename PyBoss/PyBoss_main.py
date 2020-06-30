#!/usr/bin/env python
# coding: utf-8


# Import os provides function for interacting with the operating system(OS)
# Import csv is a module for importing and reading csv files
# Import datetime to change the format of the DOB
import os
import csv
import datetime

# Provides the path of the csv file "budget-data.csv"
emp_data = os.path.join("Resources", "employee_data.csv")


# List of states and abbreviations from link provided in assignment
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# Lists to store data
firstname = []
lastname = []
empid = []
employeedob = []
employeessn = []
employeest = []


# Opens up the csvfile from the data_budget path provided above
# CSVreader iterates over each line of the csvfile
with open(emp_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Next(csvreader) just reads over the header; removing it from calculations/results
    csv_header = next(csvreader)
    
    # Going through each row after the header and first_row
    for row in csvreader:
        
        # Employee id
        empid.append(row[0])
        
        # Split first and last name by using rsplit()
        name = row[1]
        fname = name.rsplit(' ',1)[0]
        firstname.append(fname)
        lname = name.rsplit(' ',1)[1]
        lastname.append(lname)
        
        # Stripped the old date format and created new date format
        newdob = datetime.datetime.strptime(row[2],"%Y-%m-%d")
        newdob = newdob.strftime("%m/%d/%Y")
        employeedob.append(newdob)
        
        # Masked the first 7 characters of ssn by split and join string methods
        split_ssn = list(row[3])
        split_ssn[0:3] = ("*","*","*")
        split_ssn[4:6] = ("*","*")
        joined_ssn = "".join(split_ssn)
        employeessn.append(joined_ssn)
        
        # Abbreviated state name
        stateabbrev = us_state_abbrev[row[4]]
        employeest.append(stateabbrev)

# Zip lists together
cleaned_csv = zip(empid,firstname,lastname,employeedob,employeessn,employeest)


# Set variable for output file
output_file = os.path.join("New Format","Reformatted.csv")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    
    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB",
                     "SSN", "State"])
    
    # Write in zipped rows
    writer.writerows(cleaned_csv)




