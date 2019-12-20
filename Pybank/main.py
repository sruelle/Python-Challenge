import os
import csv

#set path to csv file
pyBank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#read the csv file
with open(pyBank_csv, 'r') as PyBankData:
    csvreader = csv.reader(PyBankData, delimiter=",")

    #skip the header
    next(csvreader, None)

    #set variables to 0 for baseline
    totalProfit = 0
    totalMonths = 0
    greatIncrease = 0
    greatDecrease = 0
    averageChange = 0
    totalChange = 0
    maximumChange = 0
    minimumChange = 0

    #set previousRow to zero as baseline
    ##must pop 1st value in monthlyChanges (1st month - baseline)
    previousRow = 0

    #set empty list for monthly change values
    monthlyChanges = []

    #loop through rows
    for row in csvreader:

        #running tally of Months
        totalMonths += 1

        #add to totalProfit
        totalProfit += int(row[1])

        #set current row as thisRow  
        thisRow = int(row[1])

        #calculate difference month-to-month (row-to-row)
        monthlyChange = thisRow - previousRow

        #adds monthly difference to monthlyChanges list
        monthlyChanges.append(monthlyChange)
        
        #set current row as previousRow for next iteration
        previousRow = int(row[1])
       # print(f"Monthly Change: ${monthlyChange}")
#print(monthlyChanges)

maximumChange = max(monthlyChanges)
minimumChange = min(monthlyChanges)

for i in range(0, len(monthlyChanges)):
    totalChange = totalChange + monthlyChanges[i]

             #check for greatest increase or decrease
    #if i['monthlyChange'] = maximumChange:
     #   greatIncrease = i['monthlyChange']
    #if i['monthyChange'] < minimumChange:
      #  greatDecrease = i['monthlyChange']

averageChange = totalChange/(totalMonths - 1)




print(f"Total Months: {totalMonths}")
print(f"Total Profit: ${totalProfit}")
print (f"Total Change: {totalChange}")
print(f"Average Change:{averageChange}")
print(f"Greatest Monthly Profit: ${greatIncrease}")
print(f"Greatest Monthly Loss: -${abs(greatDecrease)}")



