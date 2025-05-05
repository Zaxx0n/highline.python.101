#!/usr/bin/env python3
# Assignment: Week 5 - Smart Energy Management System for Home Appliances
# Author: Zachary Derrick                    
# Date of latest revision:  5/4/2025   
# Purpose: Develop a program that mimics a simple energy management system
#          for three home appliances: Air Conditioner, Television, and Lights.
# Resources: A04 - While Word Document, ChatGPT assited me in putting together some error handling. 
#            It reccommended the strip method combined with lower to handle if someone entered caps.
# Notes: I think there is probably a better way to do this than to use this many functions. If I had more time, 
#        I would add the ability to control separate rooms. Have options for the kitchen and such. 

# welcome message
print("🏠🌱 Welcome to Super Duper Eco House 3000 🌱🏠")

# function to get temperature
def get_temp():
    while True:
        try:
            temp = float(input("Enter the current room temperature (°F): "))
            return temp
        except ValueError:
            print("A valid temperature was not entered. Please enter a valid number.")

# checks for room occupants
def room_occupied():
    while True:
        using_room = input("Is anyone in the room? (yes/no): ").strip().lower()
        if using_room in ['yes', 'no']:
            return using_room
        print("Please enter 'yes' or 'no'.")
# gets tv preferences
def get_tv_pref():
    while True:
        watch_tv = input("Would you like to watch TV? (yes/no): ").strip().lower()
        if watch_tv in ['yes', 'no']:
            return watch_tv
        print("Please enter 'yes' or 'no'.")

# gets number of people 
def get_num_people():
    while True:
        try:
            num_people = int(input("How many people are in the room? "))
            return num_people
        except ValueError:
            print("Please try again and enter a valid number.")

# used for the final printing for aircon, tv and lights
def aircon_controller(temp, people_present):
    if temp > 75 and people_present == 'yes':
        return "Running"
    elif temp < 60 or people_present == 'no':
        return "Off"
    else:
        return "Standby"

def control_tv(people_present):
    if people_present == 'yes':
        tv_on = get_tv_pref()
        return "On" if tv_on == 'yes' else "Off"
    return "Off"

def control_lights(people_present):
    if people_present == 'yes':
        num_people = get_num_people()
        return "On" if num_people >= 1 else "Off"
    return "Off"

# handles final printing
def print_device_status(ac_status, tv_status, light_status):
    print("\n--- 📟 Smart Status Report ---")
    print(f"❄️  Air Conditioner: {ac_status}")
    print(f"📺 Television: {tv_status}")
    print(f"💡 Lights: {light_status}")

def main():
    while True:
        print("\n🌿Eco 3000 Status Report🌿")

        # gets the input for temp and people
        temp = get_temp()
        people_present = room_occupied()

        # device controls from answers
        ac_status = aircon_controller(temp, people_present)
        tv_status = control_tv(people_present)
        light_status = control_lights(people_present)

        # print function
        print_device_status(ac_status, tv_status, light_status)

        # check if they want to make changes (this is the verbage I went with for "room conditions")
        while True:
            update = input("\nWould you like to update any of your choices? (yes/no):").strip().lower()
            if update in ['yes', 'no']:
                break
            print("Please enter 'yes' or 'no'.")

        if update == 'no':
            print("Exiting Eco House 3000. Beep Boop Bop.. 🤖📡🔊")
            break

# runs the program
main()
