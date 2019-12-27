#Import objects
import os
import csv

#Set the path for the csv file
file_path = os.path.join('..', 'Resources', 'budget_data.csv')

#Initiate lists
list_month = []
list_profit_loss = []
list_profit_change = []

#Initiate variables
total_months = 0
total_profit_loss = 0
avg_change = 0
total_changes = 0
greatest_increase = 0
greatest_decrease = 0
i = 0

#Open and read csv file
with open(file_path,newline="",encoding="utf8") as budget_data:
    budget = csv.reader(budget_data,delimiter=',')

    #Skip the header
    budget_header = next(budget)

    #Sum the profit_loss values and create separate lists for each row
    for row in budget:
        total_profit_loss += int(row[1])
        total_months += 1

        list_month.append(row[0])
        list_profit_loss.append(int(row[1]))

    #Loop through the lists
    while i < len(list_month):

        if ((i+1) < len(list_month)):

            profit_diff = (list_profit_loss[i+1]) - (list_profit_loss[i])

            #Create a list of the profit/loss changes
            list_profit_change.append(profit_diff)

            #Determine if the difference is the greatest increase or decrease
            if profit_diff > greatest_increase:
                greatest_increase = profit_diff
                greatest_increase_month = list_month[i+1]
            if profit_diff < greatest_decrease:
                greatest_decrease = profit_diff
                greatest_decrease_month = list_month[i+1]

        i += 1

    #Loop through profit change list to determine thw average
    i = 0
    while i < len(list_profit_change):
        total_changes += list_profit_change[i]
        i += 1

    avg_change = total_changes / len(list_profit_change)

#Display the results on the terminal
print(f'---text')
print(f'Financial Analysis')
print(f'--------------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_loss}')
print(f'Average Change: ${round(avg_change,2)}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
print(f'---')


#Write the results  to text file
Budget_File = open('Profit_Loss.txt','a')

Budget_File.write('---text \n')
Budget_File.write('Financial Analysis \n')
Budget_File.write('-------------------------------------- \n')
Budget_File.write(f'Total Months: {total_months} \n')
Budget_File.write(f'Total: ${total_profit_loss} \n')
Budget_File.write(f'Average Change: ${round(avg_change,2)} \n')
Budget_File.write(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase}) \n')
Budget_File.write(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease}) \n')
Budget_File.write(f'--- \n')


Budget_File.close()
