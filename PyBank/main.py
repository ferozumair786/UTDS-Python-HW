import os
import csv
import random

#import file
banking = os.path.join("budget_data.csv")

#Set variables
months = 0
total = 0
profit = []
difference = 0
dates = []

#delta doesn't start out empty to keep the same number of items as the original csv
#this helps when we zip the two lists
delta = [0]
maximum = 0
minimum = 0
datemax = str(0)
datemin = str(0)
sumdelta = 0
average = 0


#open the file and set header
with open(banking,newline="") as bankfile:
    bankreader = csv.reader(bankfile,delimiter=",")
    header = next(bankreader)
    
    #Loop through csv
    for row in bankreader:

            #count number of months and total 
            months = months + 1
            total = total + int(row[1])

            #copy dates and profits into separate lists to be manipulated later
            profit.append(int(row[1]))
            dates.append(row[0])

    #loop over the profits list
    for amount in profit:
        
        #only calcilate difference once we are past the first row 
         if amount != profit[0]:
             difference = amount - profit[-1]
             delta.append(difference)

    #simultaneous loop over delta and dates lists
    for dolla, date in zip(delta, dates):
        
        #sum the differences for later calculation
        sumdelta = sumdelta + dolla
        
        #store greatest increase value and corresponding date
        if dolla > maximum:
            maximum = dolla
            datemax = date

        #store greatest decrease value and corresponding date    
        if dolla < minimum:
            minimum = dolla
            datemin = date

    #the average change is the sum of change between every month divided by total months -1
    average = sumdelta/(months-1)
    
    #trying to save space with very few print statements
    print("Financial Analysis\n---------------------------------")
    
    print(f"Total Months: {months}\nTotal: ${total}\nAverage Change: ${round(average)}")
    
    #used the actual delta values for differences because they made more sense here than the profit value
    print(f"Greatest Increase in Profits: {datemax} (${maximum})\nGreatest Decrease in Profits: {datemin} (${minimum})")

with open('bank_analysis.txt', 'w') as resultfile:
        #resultwriter = csv.writer(resultfile, delimiter = ',')
        resultfile.write("Financial Analysis\n---------------------------------\n")
        resultfile.write(f"Total Months: {months}\nTotal: ${total}\nAverage Change: ${round(average)}\n")
        resultfile.write(f"Greatest Increase in Profits: {datemax} (${maximum})\nGreatest Decrease in Profits: {datemin} (${minimum})\n")
       




