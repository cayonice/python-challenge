import os
import csv

#Data path is to financial data
budget_csv = os.path.join('budget_data.csv')
#Reading csv file and start a list of cell values for c1, the date column
with open(budget_csv, "r") as csv_file:
    c1 = []
#Delimiter data
    csvreader = csv.reader(csv_file, delimiter=',')
#Reset values
    total = 0
    months = 0
#Skip header and start with row data
    header = next(csvreader)
#Loop for rows
    for row in csv.reader(csv_file):
#Append to list
        c1.append(row[1])
#Calculate total profit or loss 
        total = total + (int(row[1]))
#Calculated how many months are included in the dataset
        months = months + 1
#Start a new list in second column   
    c2 = []
    for x, y in zip(c1, c1[1:]):
        c2.append(int(y) - int(x))
#Calculate the average and divided by the months calculated in c1
total_change = sum(c2)
average = total_change / months
#Calculate the greatest increase or decrease in profits
greatest_increase = max(c2)
greatest_decrease = min(c2)

#Print results on terminal
print("Financial Analysis")
print("------------------------")
print("Total Months: " + str(months))
print("Total: " + str(total))
#The average change in "Profit/Losses" between months over the entire period
print("Average Change: "+ str(average))
#The greatest increase in profits (date and amount) over the entire period
print("Greatest Increase in Profits: " + str(greatest_increase))
#The greatest decrease in losses (date and amount) over the entire period
print("Greatest Decrease in Profits: " + str(greatest_decrease))

#Output resulsts to text file
output_file = open("bank.txt", "w")
output_file.write("Financial Analysis\n")
output_file.write("------------------------\n")
output_file.write("Total Months: " + str(months) + "\n")
output_file.write("Total: " + str(total) + "\n")
output_file.write("Average Change: " + str(average) + "\n")
output_file.write("Greatest Increase in Profits: " + str(greatest_increase) + "\n")
output_file.write("Greatest Decrease in Profits: " + str(greatest_decrease) + "\n")
output_file.close()
