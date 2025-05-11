#!/usr/bin/env python3
# Assignment: Week 3 - Grocery Budget Calculator
# Author: Zachary Derrick                    
# Date of latest revision:  4/14/2025   
# Purpose:To understand the basic concepts of variables, int(), float(), and input() in Python 
#         by creating a real-world application - a grocery budget calculator.
# Resources: A02B - Grocery Budget Calculator
#            
# Notes: Because there is so much repetition in what the code is supposed to do, I decided to make a loop and a function.
#        There is a version of this that I was working on that uses the os library and loads a log so that previous months
#        could be imported or compared.  I eventually just simplified it to the scritp below. I would have also liked to 
#        create some way to handle error, like in the case of the user entered a string into the price prompt. 

# libraries
import math

# functions
def get_item_info(item_num):
    item = input(f"Item {item_num} name: ")
    print(item)
    qty = int(input("quantity: "))
    price = float(input(f"price of {item}: $"))
    total = qty * price
    return item, total

# main
# below the user inputs their budget and is presented with information about the following steps
monthly_budget = float(input("How much is your monthly budget: $"))
print("Next we need to gather some information. Please enter three items you've recently purchased:")
# the loop uses the following empty list to append to and starts the total expenditure as variable 0
item_totals = []
total_expenditure = 0
# for loop: I used a for loop because of the repition in my original code this loop uses the fuction get_item_info
# three times, or a range of (1, 4)
for i in range(1, 4):
    item_name, item_total = get_item_info(i)
    item_totals.append((item_name, item_total))
    total_expenditure += item_total

# prints all of the collected information using a for loop
print("\nBreakdown of individual item totals:")
for name, total in item_totals:
    print(f"{name}: ${total:.2f}")

remaining_budget = float(monthly_budget - total_expenditure)

print(f"\nYour total expenditure is: ${total_expenditure:.2f}")
print(f"Your remaining budget is: ${remaining_budget:.2f}")
