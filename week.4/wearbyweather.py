#!/usr/bin/env python3
# Assignment: Week 4 - Weather Recommender System
# Author(s): Mubashir Bholat, Zachary Derrick                    
# Date of latest revision:  4/25/2025   
# Purpose: The user will input the current temperature and whether it's
#          raining or not. Based on the input, your program
#          will recommend appropriate clothing.
# Resources: A03 - If/Else - Weather Recommender System
# Notes: We were able to fit this assignment into a single function that also has error handling using try/except.
#        I think giving the program the option to input Fahrenheit would make it more usable. I could see a stretch 
#        goal of having the user input clothes that they enjoy wearing and having the program select from that list or
#        giving the user a big variety of clothes as options. I have little experience using APIs, but if this program 
#        could reach out to a national weather service, we could automate a lot more.

# A function called weatherwear
def weatherwear():
    try: # try along with except helps us with error handling
        temp = float(input("Enter the current temperature in Celsius: "))
        # we went with while loops to handle the rain and wind options
        while True:
            print("Is it raining?")
            print("1. Yes")
            print("2. No")
            raining = input("Enter 1 or 2: ")
            if raining in ["1", "2"]:
                break
            else:
                print("That is not a valid option. Please try again by entering 1 or 2.")

        while True:
            print("Is it windy?")
            print("1. Yes")
            print("2. No")
            windy = input("Enter 1 or 2: ")
            if windy in ["1", "2"]:
                break
            else:
                print("That is not a valid option. Please try again by entering 1 or 2.")

        # Temperature-based recommendations
        # Print statements at the end so to handle order of recommendations
        if temp < 10:
            print("Due to cold weather, I recommend wearing a heavy jacket or sweater.")
        elif 10 <= temp <= 25:
            print("It's pleasant today. Try wearing a light jacket or t-shirt.")
        else:
            print("Today's weather is rather hot. Wear shorts and a t-shirt or something light and comfortable.")

        # Rain-based recommendation
        if raining == "1":
            print("Carry an umbrella today and be sure to wear waterproof shoes.")

        # Wind-based recommendation
        if windy == "1":
            print("It's windy outside. Consider wearing a windbreaker or a scarf.")

    except ValueError:
        print("Please enter a valid number for temperature.")

# Call the function
weatherwear()