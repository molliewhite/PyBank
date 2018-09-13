import os
import csv

csvpath = os.path.join('budget_data.csv')

total_months = 0
total_revenue = 0
greatest_inc = 0
greatest_inc_date = ""
greatest_dec = 0
greatest_dec_date = ""


with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)

    for row in csvreader:
        total_months += 1
        total_revenue += int(row[1])
        if int(row[1]) >= greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_date = row[0]
        if int(row[1]) <= greatest_dec:
            greatest_dec = int(row[1])
            greatest_dec_date = row[0]
    
    



average_change = round(total_revenue/total_months, 2)


print("Financial Analysis")
print("--------------------------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: $" + str(total_revenue))
print("Average Revenue Change: $" + str(average_change))
print("Greatest Increase in Revenue: " + greatest_inc_date + " ($" + str(greatest_inc) + ")")
print("Greatest Decrease in Revenue: " + greatest_dec_date + " ($" + str(greatest_dec) + ")")



newoutput = open("newoutput.txt", "w")

# writing the text file
newoutput.write("Financial Analysis \n")
newoutput.write("-------------------------------------------- \n")
newoutput.write("Total Months: " + str(total_months) + "\n")
newoutput.write("Total Revenue: $" + str(total_revenue) + "\n")
newoutput.write("Average Revenue Change: $" + str(average_change) + "\n")
newoutput.write("Greatest Increase in Revenue: " + greatest_inc_date + " ($" + str(greatest_inc) + ")" + "\n")
newoutput.write("Greatest Decrease in Revenue: " + greatest_dec_date + " ($" + str(greatest_dec) + ")" + "\n")


