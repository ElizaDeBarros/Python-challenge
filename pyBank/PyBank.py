import os
import csv

# Create a path for budget_data file
csv_path = os.path.join('Resources', 'budget_data.csv')

# create a list to store number of rows
number_rows = []
change_list = []
temp_list = []

# For increments
Net_ProfitLoss = 0
Change = 0.0

index_min = 0
index_max = 0
min_date = ""
max_date = ""
count = 0

# empty list to receive values of changing in Profit/Loss
changing_PL = []

# Read csv file
with open(csv_path, 'r', newline="") as csvfile:
    # file handler with list of rows
    csvreader = csv.reader(csvfile)
    # Skips header
    csv_header = next(csvreader, None)
    for row in csvreader: # loop into rows of the file
        number_rows.append(row) # add row numbers to the list number_rows
        change_list.append(row[1]) # creates a list with elements of the second column of input file only
        Net_ProfitLoss = int(row[1]) + Net_ProfitLoss

for i in range(len(change_list)-1): # loops from 0 to 85 on the changeList
    Change = ((float(change_list[i + 1]) - float(change_list[i])) + Change)  # increments Change by adding the difference of two subsequent values
    changing_PL.append(float(change_list[i + 1]) - float(change_list[i])) # adds the difference of two subsequent values to the list changing_PL
Change = round((Change /(i+1)),2)

min_elem = changing_PL[0]
max_elem = changing_PL[0]

for i in range(1,len(changing_PL)-1):
    if changing_PL[i] < min_elem:
        min_elem = changing_PL[i]
        index_min = i + 2
    if changing_PL[i] > max_elem:
        max_elem = changing_PL[i]
        index_max = i + 2
min_elem = round(min_elem, 0)
max_elem = round(min_elem, 0)

with open(csv_path, 'r', newline="") as csvfile:
    # file handler with list of rows
    csvreader = csv.reader(csvfile)
    # Skips header
    csv_header = next(csvreader, None)
    for row in csvreader:
        temp_list.append(row)
        count = len(temp_list)
        if count == index_min:
            min_date = row[0]
        if count == index_max:
            max_date = row[0]


print("Total Months: " + str(len(number_rows)))
print("The total net profit/loss is $" + str(Net_ProfitLoss))
print("Average Change: $" + str(Change))
print("Greatest Increase in Profits: " + max_date + "   ($" + str(max_elem) + ")")
print("Greatest Decrease in Profits: " + min_date + "   ($" + str(min_elem) + ")")

elem1 = "Total Months: " + str(len(number_rows))
elem2 = "The total net profit/loss is $" + str(Net_ProfitLoss)
elem3 = "Average Change: $" + str(Change)
elem4 = "Greatest Increase in Profits: " + max_date + "   ($" + str(max_elem) + ")"
elem5 = "Greatest Decrease in Profits: " + min_date + "   ($" + str(min_elem) + ")"


textList = [elem1,elem2,elem3,elem4,elem5]
os.mkdir('Analysis')
output_path = os.path.join('Analysis', 'analysis_results.txt')
out = open(output_path, 'w', newline="")
for line in textList:
    out.write(line)
    out.write("\n")
out.close()
