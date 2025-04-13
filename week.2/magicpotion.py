#!/usr/bin/env python3
# Assignment: Week 2 - Magic Potion Recipe
# Author: Zachary Derrick                    
# Date of latest revision:  4/13/2025   
# Purpose: Write a Python program that takes in user input for
#          a few pieces of data, calculates the needed amount of each ingredient,
#          and outputs a magic potion recipe.
# Resources: A02A - Magic Potion Recipe Word Document, ChatGPT, 
#            Variables and Print Sample: https://youtu.be/03MGu250mqU?si=HHj-IILJ-xc-nsse
# Notes: I decided to go with a menu that allows the user to select from 
#        a list of cauldrons. An advanced version of this would allow the user to
#        input their own cauldron name and its size as an additional option.

# libraries
import math

# main
cauldrons = [
    {"cauldronName": "Pixie Pan " + "🧚", "cleanName": "Pixie Pan", "size": .50},      
    {"cauldronName": "Goblin Goblet 🧌 ", "cleanName": "Goblin Goblet", "size": 1},  
    {"cauldronName": "Witchfire Basin 🔥", "cleanName": "Witchfire Basin", "size": 2.5},
    {"cauldronName": "Elder Warlock Vat 🔮", "cleanName": "Elder Warlock Vat", "size": 5},  
    {"cauldronName": "Dragon Tea Kettle 🐉", "cleanName": "Dragon Tea Kettle", "size": 10}    
]

# gives the user a list of common caudrons to choose from and includes
# its size in liters
print("Common Cauldrons:")
# enumerate takes a list and returns pairs of index and value, here cauldruns and its number in the list
for i, cauldron in enumerate(cauldrons, 1):
    liters = cauldron["size"] 
    print(f"{i}) {cauldron['cauldronName']} — {liters} Liters")

# user selection
while True:
    try:
        choice = int(input("Which cauldron are you using for your brew?: "))
        if 1 <= choice <= len(cauldrons):
            selectedCauldron = cauldrons[choice - 1]
            break
        else:
            print("That is not an option.")
    except ValueError:
        print("Please enter a number from the list. (1-5)")

potionLiters =  selectedCauldron["size"]

# get number of plants
plants = int(input("How many plants will you be growing?: "))
# we need to check if the plants are an even number for later so this makes sure the number 
# of plants is divisible by 2 with no remainder
evenPlants = plants if plants % 2 == 0 else plants + 1

# calculations
crystalWater = 0.5 * potionLiters
# roundedWater = math.ceil(crystalWater * 100) / 100  - I was playing around with rounding to the nearest hundredth 
moonDust = 10 * plants
sunflowerPetals = (evenPlants // 2) * 3
# math.ceil rounds up the result to the nearest whole number since we area using eyes as a counter
eyeofNewt = math.ceil(sunflowerPetals / 5)
# print the recipe to the screen. 
print(f"\n🧪 Ingredients Needed to Grow {plants} Plants Using Your {selectedCauldron['cleanName']}: ")
# the ':.2f' gives the answer in float with 2 digits after the decimal point
print(f"- Crystal Water: {crystalWater:.2f} Liters")
print(f"- Moon Dust: {moonDust} Grams")
print(f"- Sunflower Petals: {sunflowerPetals} Petals")
print(f"- Eye of Newt: {eyeofNewt} Eyeballs")