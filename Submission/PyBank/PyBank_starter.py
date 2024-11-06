# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

filepath = "Pybank/Resources/budget_data.csv"
outputpath = "PyBank/analysis/budget_analysis.txt"

months = 0
net = 0
last_profit = 0
current_profit = 0
current_change = 0
most_change = 0 
least_change = 0
most_change_month = ""
least_change_month = ""
first_month_profit = 0


with open(filepath) as csvfile:


    csvreader = csv.reader(csvfile, delimiter=',')

    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

   
    for row in csvreader:
        months +=1
        current_profit = int(row[1])
        net += current_profit
        if months == 1: 
            current_change = 0
            first_month_profit = current_profit
        else:
            current_change = current_profit - last_profit
            if current_change > most_change:
                most_change = current_change
                most_change_month = row[0]
            if current_change < least_change:
                least_change = current_change
                least_change_month = row[0]
        last_profit = current_profit



    output = f"""
    Financial Analysis
    Total Months: {months}
    Total: ${net}
    Average Change: ${round((current_profit - first_month_profit) / (months - 1),2)}
    Greatest Increase in Profits: {most_change_month} ${most_change}
    Greatest Decrease in Profits: {least_change_month} ${least_change}
    """

    print(output)
with open(outputpath,"w") as outputtxt:
    outputtxt.write(output)