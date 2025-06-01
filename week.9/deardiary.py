#!/usr/bin/env python3
# Assignment: Week 9 - Personal Diary Management System
# Author: Zachary Derrick                    
# Date of latest revision:  5/31/2025   
# Purpose: Create a Python program that simulates a personal diary management system. The program will allow a user to 
#          record, read, and manage their daily diary entries. 
#          This exercise will test your understanding of file operations and exception handling in Python.
# Resources: A08 - File - Diary Document, OpenAI - helped in making rainbow text. 
#            I also use OpenAI for quick emoji reference and suggestions.
# Notes:   I wanted to make this colorful so I bounced ideas off of OpenAI on how to
#          best make a rainbow text thoughout the program.  This went though multiple
#          iterations before settling on the colorsys library, a first for me. I also
#          liked the idea of playing around with a password to protect the diary.  
#          This password is stored as plain text in the variable PASSWORD and thus not
#          encrypted. Also, I've used datetime in some of my security scripts before, 
#          so I wanted to have the option to have the date added automatically. 
#          Throughout the program I use 'utf-8' encoding to ensure characters are saved and read correctly, minimizing errors
#          An easy stretch goal would be to add user handling to this program. I was reading my last comment about
#          jokingly sending a message to the user and thought it would be nice to put the user's name there.

# modules
import os
from datetime import datetime

dear_diary_file = "deardiary.txt"

def reading_rainbow(text):
    from colorsys import hsv_to_rgb

    result = ""
    reset = "\033[0m"
    n = len(text)

    for i, char in enumerate(text):
# This picks a color along the rainbow for each character by spreading out the hue evenly,
# converts it to RGB, then adds the colored character to the result string.
# At the end, it resets the colors before returning the full colored text.
        hue = (i / max(n - 1, 1)) * 0.85  
        r, g, b = [int(x * 255) for x in hsv_to_rgb(hue, 1, 1)]
        result += f"\033[38;2;{r};{g};{b}m{char}"
    result += reset
    return result

# red print for errors and warnings
def red_print(text):
    bright_red = "\033[91m"
    reset = "\033[0m"
    print(f"{bright_red}{text}{reset}")

# takes the reading rainbow function to color text in a rainbow pattern
# this is a seperate function for flexibility 
def rainbow_print(text):
    print(reading_rainbow(text))

# this program uses psudo password protection, below handles the recording of a failed attemp(s)
def record_failed_attempt():
    try:
        with open(dear_diary_file, "a", encoding='utf-8') as f:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"FAILED_PASSWORD_ATTEMPT {now}\n")
    except Exception as e:
        print("Error recording failed attempt:", e)

# my program records failed attempts, this is the fucntion that checks the first line of the .txt file
# if it finds a failed attempt it will report that and then remove it so that it doesn't always report 
# failed attempts after a first
def check_failed_attempt():
    try:
        with open(dear_diary_file, "r", encoding='utf-8') as f:
            lines = f.readlines()

            # looks for lines that log failed password attempts
        failed_attempts = [line for line in lines if line.startswith("FAILED_PASSWORD_ATTEMPT")]
        if failed_attempts:
            # removes failed attempt lines so they're only reported once        
            lines = [line for line in lines if not line.startswith("FAILED_PASSWORD_ATTEMPT")]
            with open(dear_diary_file, "w", encoding='utf-8') as f:
                f.writelines(lines)

            # returns the datetime so the user can know when the failed attempt happened
            last_attempt = failed_attempts[-1].strip().split(" ", 1)[1]
            return last_attempt
    except FileNotFoundError:
        return None
    except Exception as e:
        print("Error checking for failed attempts:", e)
    return None

# my main menu starts by checking for failed attempts to report back to the user, added some emoji,
# this is a menu system I've used many times before
def main_menu():
    failed_time = check_failed_attempt()
    
    if failed_time:
        red_print(f"\n⚠️  WARNING: SOMEONE TRIED TO READ YOUR DIARY!! Failed Attempt: {failed_time}  ⚠️\n")
    print("💌🎀🌈" + reading_rainbow("Dear Diary") + "🌈🎀💌")
    while True:
        rainbow_print("\nMake a Selection from Below:")
        rainbow_print("    1) ✍️ Create New Entry")
        rainbow_print("    2) 📖 Read Latest Entry")
        rainbow_print("    3) 📚 Read All Entries")
        rainbow_print("    4) 🗑️ Delete the Latest Entry")
        rainbow_print("    5) 🌙 Quit Program\n")
        
        selected_main_option = input("> ")
        rainbow_print(f"You have selected option:{selected_main_option}")
        if selected_main_option == '1':
            create_new_entry()
        elif selected_main_option == '2':
            read_latest_entry()
        elif selected_main_option == '3':
            read_all_entries()
        elif selected_main_option == '4':
            delete_latest_entry()
        elif selected_main_option == '5':
            rainbow_print("🔒Your Secrets Are Safe With Me, Bye!🔒")
            exit()
        else:
            red_print("Invalid option. Please try again.")

# function for creating the new diary entry;
# lets the user type a date or press Enter to use today's date; 
# uses sanitization to make sure the entries are consistant
def create_new_entry():
    try:
        while True:
            date_input = input(reading_rainbow("Enter the date (e.g. 2025-05-31) or press Enter to use today's date: "))
            if not date_input.strip():
                date = datetime.now().strftime("%Y-%m-%d")
                break
            else:
                try:
                    # check to see if the user gave us a valid date
                    valid_date = datetime.strptime(date_input.strip(), "%Y-%m-%d")
                    date = valid_date.strftime("%Y-%m-%d")  # sanitizes and normalizes the date input
                    break
                except ValueError:
                    red_print("Invalid date format. Please enter the date like 2025-05-31 or press Enter to add system's date.")
        
        entry = input("Write your diary entry:\n")
        with open(dear_diary_file, "a", encoding='utf-8') as f:
            f.write(f"--- {date} ---\n{entry}\n\n")
        rainbow_print("Entry added successfully!")
    except Exception as e:
        red_print(f"Failed to write entry: {e}")

# handles retrieving the most recent diary entry by accessing the last item in the list ([-1])and informs user if there are none
def read_latest_entry():
    try:
        with open(dear_diary_file, "r", encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                rainbow_print("No diary entries yet.")
                return
            entries = content.split("\n\n")
            rainbow_print("Latest Entry:\n" + entries[-1])
    except FileNotFoundError:
        red_print("Diary file not found.")
    except Exception as e:
        red_print("Failed to read latest entry:", e)

# handles retrieving all diary entries and informs user if there are none
def read_all_entries():
    try:
        with open(dear_diary_file, "r", encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                print("📝 No diary entries yet.")
                return
            rainbow_print("📖 All Entries:\n" + content)
    except FileNotFoundError:
        red_print("Diary file not found.")
    except Exception as e:
        red_print("Failed to read entries:", e)

# handles deleting the last entry
def delete_latest_entry():
    try:
        with open(dear_diary_file, "r", encoding='utf-8') as f:
            content = f.read().strip()
        if not content:
            rainbow_print("No entries to delete.")
            return
        entries = content.split("\n\n")
        deleted_entry = entries.pop()
        with open(dear_diary_file, "w", encoding='utf-8') as f:
            f.write("\n\n".join(entries) + ("\n" if entries else ""))
        rainbow_print("🗑️ Deleted latest entry:\n" + deleted_entry)
    except FileNotFoundError:
        red_print("Diary file not found.")
    except Exception as e:
        red_print("Failed to delete entry:", e)

def dear_diary_exists():
    if not os.path.exists(dear_diary_file):
        try:
            with open(dear_diary_file, "w") as f:
                pass  # Just create the file
        except Exception as e:
            print("Error initializing diary file:", e)

# here is my basic password check, we don't use any encryption
def check_password():
    PASSWORD = "solarwinds123"
    attempt = input("Enter super secret password: ")
    if attempt == PASSWORD:
        return True
    else:
        record_failed_attempt()
        print("That is not the super secret password!")
        return False

# starts the program by using an if condition for a simple password check and checks if deardiary.txt has been created
if check_password():
    dear_diary_exists()
    main_menu()
else:
    # says that it sends a message just to panic the snoop XD
    rainbow_print("My secrets are safe from you!!! Sending message of failed attempt to owner!")
    exit()





