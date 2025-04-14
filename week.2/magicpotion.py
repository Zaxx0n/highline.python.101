#!/usr/bin/env python3
# Assignment: Week 2 - Magic Potion Recipe
# Author: Zachary Derrick                    
# Date of latest revision:  4/13/2025   
# Purpose: Write a Python program that takes in user input for
#          a few pieces of data, calculates the needed amount of each ingredient,
#          and outputs a magic potion recipe.
# Resources: A02A - Magic Potion Recipe Word Document
#            ChatGPT helped create the menu system https://chatgpt.com/share/67fc4030-6ca8-800c-bed4-6c28e3b7350d 
#            Variables and Print Sample: https://youtu.be/03MGu250mqU?si=HHj-IILJ-xc-nsse
# Notes: I decided to go with a menu that allows the user to select from 
#        a list of cauldrons. An advanced version of this would allow the user to
#        input their own cauldron name and its size as an option.

# libraries
import math
import random

# main

# created some cauldron names and added some emoji for each 
# had help from ChatGPT creating this. I didn't want the emoji later, so I included a cleanName
cauldrons = [
    {"cauldronName": "Pixie Thimble  🧚", "cleanName": "Pixie Thimble", "size": 2},      
    {"cauldronName": "Goblin Goblet 🧌 ", "cleanName": "Goblin Goblet", "size": 4},  
    {"cauldronName": "Witchfire Basin 🔥", "cleanName": "Witchfire Basin", "size": 7.5},
    {"cauldronName": "Warlock Tub 🔮", "cleanName": "Warlock Tub", "size": 10},  
    {"cauldronName": "Dragon Tea Kettle 🐉", "cleanName": "Dragon Tea Kettle", "size": 50}    
]


print("Eldritch Line Cauldrons:")

# creates the list
for i, cauldron in enumerate(cauldrons, 1): # enumerate takes a list and returns pairs of index and value
    liters = cauldron["size"] 
    print(f"{i}) {cauldron['cauldronName']}\t — {liters} Liters")

# user selection
while True:
    try:
        choice = int(input("Which cauldron are you using for your brew?: "))
        if 1 <= choice <= len(cauldrons):
            userCauldron = cauldrons[choice - 1]
            break
        else:
            print("That is not an option.")
    except ValueError:
        print("Please enter a number from the list. (1-5)")

potion_liters =  userCauldron["size"]

# get number of plants
plants = int(input("How many plants will you be growing?: "))
# we need to check if the plants are an even number for later so this makes sure the number of
# plants is divisible by 2 with no remainder
adjustedPlants = plants if plants % 2 == 0 else plants + 1

# calculations
crystal_water = 0.5 * potion_liters
moon_dust = 10 * plants
sunflower_petals = (adjustedPlants // 2) * 3
# math.ceil rounds up the result to the nearest whole number since we area using eyes as a counter
eye_of_newt = math.ceil(sunflower_petals / 5)
# wanted to use math.pi and random numbers
hyssop = random.randint(1, 100)  / math.pi * 10

# print the recipe to the screen. 
print(f"\nIngredients Needed to Grow {plants} Plants Using Your {userCauldron['cleanName']}: ")
print(f"💎 - Crystal Water: {crystal_water} Liters")
print(f"🌙 - Moon Dust: {moon_dust} Grams")
print(f"🌻 - Sunflower Petals: {sunflower_petals} Petals")
print(f"🦎 - Eye of Newt: {eye_of_newt} Eyeballs")
print(f"🪻  - Hyssop: {hyssop:.3f} Pinches of Ground Root") # this will not be a whole number, just for the sillyness
print(f"\n\033[91mRemember, witchlings, magic is not to be trifled with! Mix your brews carefully, or face the consequences!\033[0m 😈✨")