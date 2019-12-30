#Import objects
import os
import csv
import re

#Set the csv file path
file_path = os.path.join('..', 'Resources', 'employee_data.csv')

#Initiate lists
list_list_emp_header = []
list_emp_ID = []
list_first_name = []
list_last_name = []
list_DOB_year = []
list_DOB_month = []
list_DOB_day = []
list_DOB = []
list_SSN = []
list_state = []

state_abbrev = ''

#Pull in the united states abbreviations
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

def pull_it_all_together():

    #initiate variables
    i = 0
    j = 0

    #Write the results to csv file
    with open('Employee_Converted_Data.csv','w') as new_employee_file:

        new_employees = csv.writer(new_employee_file, delimiter=',')

        #Write headers
        new_employees.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])

        while i < len(list_emp_ID):

            new_employees.writerow([list_emp_ID[i],list_first_name[i],list_last_name[i],list_DOB[i],list_SSN[i],list_state[i]])

            i += 1

    return

#Open and read csv file
with open(file_path,newline="",encoding="utf8") as employee_data:
    employees = csv.reader(employee_data,delimiter=',')

    #Store the file header
    list_emp_header = next(employees)

    #Pull the employee data and manipulate
    for row in employees:

        list_emp_ID.append(row[0])

        list_first_name.append(row[1].split(' ')[0])
        list_last_name.append(row[1].split(' ')[1])

        list_DOB.append(row[2].split('-')[1] + '/' + row[2].split('-')[2] + '/' + row[2].split('-')[0])

        list_SSN.append(re.sub('(?:\d{3})-(?:\d{2})','***-**',row[3]))

        list_state.append(us_state_abbrev[row[4]])

pull_it_all_together()
