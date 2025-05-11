#!/usr/bin/env python3
# Assignment: Week 6 - Temperature Conversion Functions
# Author: Zachary Derrick                    
# Date of latest revision:  5/11/2025   
# Purpose: To understand the working of functions in Python by creating 
#          simple real-world temperature conversion utilities.
# Resources: A05 - Functions Temperature Word Document, Revised Menu from My Attacktools Script  
# Notes: This is a menu that I've used in programs outside of this class.
#        It's simple and I thought it fit in nicely for this assignment. 

# functions for conversion
def celsius_to_fahrenheit():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is {fahrenheit:.2f}°F\n")
    except ValueError:
        print("Invalid input. Please try again.\n") # error handling

def fahrenheit_to_celsius():
    try:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is {celsius:.2f}°C\n")
    except ValueError:
        print("Invalid input. Please try again.\n") # error handling

# basic menu for conversion selection
while True:
    print("Neato Temperature Conversion Tool")
    print("🌞🌞🌞🌞🌞🌞🌞🌞")

    conversion = input("""\nSelect Conversion to Make:
                1) Celsius to Fahrenheit
                2) Fahrenheit to Celsius
                3) Exit Program      
                \n""").strip()

    if conversion == "1":
        celsius_to_fahrenheit()
    elif conversion == "2":
        fahrenheit_to_celsius()
    elif conversion == "3":
        print(f"Thank you for using the Neato Conversion Program! \n" 
        "Exiting Now")
        break
    else:
        print("Invalid selection. Please enter 1, 2, or 3.\n")

