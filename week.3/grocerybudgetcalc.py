#!/usr/bin/env python3
# Assignment: Week 3 - Grocery Budget Calculator
# Author: Zachary Derrick                    
# Date of latest revision:  4/14/2025   
# Purpose:To understand the basic concepts of variables, int(), float(), and input() in Python 
#         by creating a real-world application - a grocery budget calculator.
# Resources: A02B - Grocery Budget Calculator
#            
# Notes: 

# libraries
import math

def get_item_info(item_num):
    item = input(f"Item {item_num} name: ")
    print(item)
    qty = int(input("quantity: "))
    price = float(input(f"price of {item}: $"))
    total = qty * price
    return item, total

monthly_budget = float(input("How much is your monthly budget: $"))

print("Next we need to gather some information. Please enter three items you've recently purchased:")

item_totals = []
total_expenditure = 0
for i in range(1, 4):
    item_name, item_total = get_item_info(i)
    item_totals.append((item_name, item_total))
    total_expenditure += item_total


print("\nBreakdown of individual item totals:")
for name, total in item_totals:
    print(f"{name}: ${total:.2f}")

remaining_budget = float(monthly_budget - total_expenditure)

rounded_expenditure = math.ceil(total_expenditure)
print(f"\nYour total expenditure is: ${total_expenditure:.2f}")
print(f"Your remaining budget is: ${remaining_budget:.2f}")

# rounded_expenditure = math.ceil(total_expenditure)
# print(f"Your total expenditure is: ${rounded_expenditure}")