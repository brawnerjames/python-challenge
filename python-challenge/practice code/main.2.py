import os
import csv

csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline="") as csvfile:
    budget_csv = csv.reader(csvfile, delimiter = ",")

    # Assign first row to be header
    budget_header = next(budget_csv)

    month_total = sum(1 for row in budget_csv)
    print(month_total)  

   
with open(csvpath, newline="") as csvfile:
    budget_csv = csv.reader(csvfile, delimiter = ",")

    budget_header = next(budget_csv)

    #Set var to 0 to iterate
    net_profit = 0
    
    # iterate over column using float function to add values and then add to var
    for row in budget_csv:
        net_profit += float(row[1])
        
    print(net_profit)
    
import pandas as pd

budget_df = pd.read_csv("budget_data.csv")

profit = budget_df.loc[:, "Profit/Losses"]

profit_diff = profit.diff()

profit_mean = profit_diff.mean()
print(profit_mean)

profit_max = profit_diff.max()
print(profit_max)

profit_min = profit_diff.min()
print(profit_min)



    



    






    

    



    

    


 

    




