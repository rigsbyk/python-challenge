#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
import datetime


# In[2]:


emp_data = os.path.join("Resources", "employee_data.csv")


# In[3]:


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


# In[4]:


firstname = []
lastname = []
empid = []
employeedob = []
employeessn = []
employeest = []


# In[5]:


with open(emp_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        #employee id
        empid.append(row[0])
        
        #split first and last name by using rsplit()
        name = row[1]
        fname = name.rsplit(' ',1)[0]
        firstname.append(fname)
        lname = name.rsplit(' ',1)[1]
        lastname.append(lname)
        
        #stripped the old date format and created new date format
        newdob = datetime.datetime.strptime(row[2],"%Y-%m-%d")
        newdob = newdob.strftime("%m/%d/%Y")
        employeedob.append(newdob)
        
        #masked the first 7 characters of ssn by split and join string methods
        split_ssn = list(row[3])
        split_ssn[0:3] = ("*","*","*")
        split_ssn[4:6] = ("*","*")
        joined_ssn = "".join(split_ssn)
        employeessn.append(joined_ssn)
        
        #abbreviated state name
        stateabbrev = us_state_abbrev[row[4]]
        employeest.append(stateabbrev)


# In[6]:


cleaned_csv = zip(empid,firstname,lastname,employeedob,employeessn,employeest)


# In[7]:


output_file = os.path.join("New Format","Reformatted.csv")


# In[8]:


with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB",
                     "SSN", "State"])
    
    writer.writerows(cleaned_csv)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




