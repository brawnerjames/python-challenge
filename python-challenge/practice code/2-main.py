import os
import csv

csvpath = os.path.join('budget_data.csv')
text_output = os.path.join('budget_analysis.txt')
    #The total number of months included in the dataset
total_months = 0

  #The net total amount of "Profit/Losses" over the entire period
total_net = 0

  #The average of the changes in "Profit/Losses" over the entire period
month_of_change = []
net_change_list = []
net_monthly_average = 0

  #The greatest increase in profits (date and amount) over the entire period
greatest_increase = ["",0]
  #The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = ["",999999999999999999999999]

with open(csvpath, newline="") as csvfile:
    budget_csv = csv.reader(csvfile, delimiter = ",")

    # Assign first row to be header
    budget_header = next(budget_csv)
    # Extract the first row to avoid appending to net_change_list
    first_row = next(budget_csv)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1])

    for row in budget_csv:

        #Track the total
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        #Track net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])

        net_change_list = net_change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        #Calculate the greatest increase

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        #Calculate the greatest decrease

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
    
    net_monthly_average = sum(net_change_list)/len(net_change_list)


output = (
f"\nFinancial Analysis\n"
 f"----------------------------\n"
  f"Total Months: {total_months}\n"
  f"Total: ${total_net}\n"
  f"Average  Change: ${net_monthly_average}\n"
  f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
  f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

print(output)
with open(text_output, "w") as txt:
    txt.write(output)