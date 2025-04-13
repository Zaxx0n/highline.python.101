#!/usr/bin/env python3
# Assignment: Week 2 - Magic Potion Recipe
# Author: Zachary Derrick                    
# Date of latest revision:  4/13/2025   
# Purpose: write a Python program that takes in user input for
#          a few data, calculates the needed amount of each ingredient,
#          and outputs a magic potion recipe.
# Resources: A02A - Magic Potion Recipe Word Document, ChatGPT, 
#            Variables and Print Sample: https://youtu.be/03MGu250mqU?si=HHj-IILJ-xc-nsse

# libraries
import math

# I decided to go with a menu that allows the user to select from 
# a list of "pots". An advanced version of this would allow the user to
# input their own cauldron and its size.
cauldrons = [
    {"cauldronName": "Pixie's Pan " + "🧚", "cleanName": "Pixie's Pan", "size": .25},      
    {"cauldronName": "Goblin's Goblet 🧌 ", "cleanName": "Goblin's Goblet", "size": 1},  
    {"cauldronName": "Witchfire Basin 🔥", "cleanName": "Witchfire Basin", "size": 2.5},
    {"cauldronName": "Elder Warlock's Vat 🔮", "cleanName": "Elder Warlock's Vat", "size": 5},  
    {"cauldronName": "Dragon's Tea Kettle 🐉", "cleanName": "Dragon's Tea Kettle", "size": 10}    
]

# gives the user a list of common caudrons to choose from and includes
# its size in liters
print("Common Cauldrons")
for i, cauldron in enumerate(cauldrons, 1):
    liters = cauldron["size"] * 5
    print(f"{i}) {cauldron['cauldronName']} — {liters} Liters")

# user selection
while True:
    try:
        choice = int(input("Which cauldron are you using for your brew?: "))
        if 1 <= choice <= len(cauldrons):
            selectedCauldron = cauldrons[choice - 1]
            break
        else:
            print("That is not a known option.")
    except ValueError:
        print("Please enter a number, Pleb.")

potSizeLiters = selectedCauldron["size"] * 5

# get number of plants
plants = int(input("How many plants will you be growing?: "))

# calculations
crystalWater = 0.5 * potSizeLiters
moonDust = 10 * plants
# math.ceil rounds the result to the nearest whole number
sunflowerPetals = math.ceil((3 * plants) / 2)
eyeofNewt = math.ceil(sunflowerPetals / 5)
# print the recipe to the screen. 
print(f"\n🧪 Ingredients Needed to Grow {plants} Plants Using Your {selectedCauldron['cleanName']}: ")
# the ':.2f' gives the answer in float with 2 digits after the decimal point
print(f"- Crystal Water: {crystalWater:.2f} Liters")
print(f"- Moon Dust: {moonDust} Grams")
print(f"- Sunflower Petals: {sunflowerPetals} Petals")
print(f"- Eye of Newt: {eyeofNewt} Eyeballs")