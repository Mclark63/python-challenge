
from netrc import netrc
import os
import csv

csvpath = "PyBank/Resources/budget_data.csv"

with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header=next(csvreader)
        first_row=next(csvreader)
       


        Total_months = 0
        Net_profit_loss = 0
      
        for row in csvreader:
                Total_months = Total_months + 1
                
                Net_profit_loss = Net_profit_loss + int(row[1])  

                 

# print(Total_months)
print(int(Total_months))

# # The net   total amount of "Profit/Losses" over the entire period
        # print("Total")

print(int(Net_profit_loss))

# # # The changes in "Profit/Losses" over the entire period, and then the average of those changes

Average_Change = Net_profit_loss/Total_months

# # print("Profit and Losses")

print(f"Average Change: {Average_Change}")


#export
with open("Pybank_export.txt", "w") as f:
        f.write("readme")


# # # The greatest increase in profits (date and amount) over the entire period
# GPC = 
# # print("Greatest Profit Increase")

# print(f"Greatest Profit Increase:{GPD} ")
# # # The greatest decrease in profits (date and amount) over the entire period
# # print("Greatest")
# print(f"Greatest Profic Decrease: {GPI} ")