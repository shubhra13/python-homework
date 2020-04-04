# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')

# Initialize list objects to hold our menu and sales data
menu = []
sales = []

# Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# Read in the menu data into the menu list
with open(menu_filepath, "r") as menufile:
    csvreader = csv.reader(menufile, delimiter=',')
    header = next(csvreader)
    for _ in csvreader:
        menu.append(_)


# Read in the sales data into the sales list        
with open(sales_filepath, "r") as salesfile:
    csvreader = csv.reader(salesfile,delimiter=',')
    header = next(csvreader)
    for _ in csvreader:
        sales.append(_)


# Loop over every row in the sales list object
for _ in sales:
    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # Initialize sales data variables
    quantity = int(_[3])
    sales_item = _[4].strip()

    # For every row in our sales data, loop over the menu records to determine a match   
    for row in menu:
        # Initialize menu data variables
        # item,category,description,price,cost
        item = row[0].strip()
        price = float(row [3])
        cost = float(row [4])
     
        # Calculate profit of each item in the menu data        
        profit = (price - cost)
        
        # If the item value not in the report, add it as a new entry with initialized metrics
        if sales_item not in report:
            report[sales_item]={"01-count": 0, "02-revenue": 0,"03-cogs": 0,"04-profit": 0}
           
        # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
        if item == sales_item: 
            
            # Cumulatively add the values to the corresponding metrics
            report[sales_item]["01-count"] += quantity
            report[sales_item]["02-revenue"] += price * quantity
            report[sales_item]["03-cogs"] += cost * quantity
            report[sales_item]["04-profit"] += profit * quantity   

        else:
            print(f'{sales_item} does not equal {item}! NO MATCH!')
        
    #Increment the row counter by 1
    row_count += 1

# Print total number of records in sales data
print(f'total number of records in sales data {row_count}')

# Write out report to a text file (won't appear on the command line output)
outputfilepath = Path("outputfile.txt")
with open(outputfilepath , "w") as outputfile:
    #outputfile.write(str(report))
    for k,v in report.items():
        outputfile.write(str(k) + str(v) + '\n')
