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

# modules
import os
from datetime import datetime

dear_diary_file = "deardiary.txt"

# this program uses multiple menus, this being the main menu
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

def red_print(text):
    RED_BRIGHT = "\033[91m"
    RESET = "\033[0m"
    print(f"{RED_BRIGHT}{text}{RESET}")

def rainbow_print(text):
    print(reading_rainbow(text))

def record_failed_attempt():
    try:
        with open(dear_diary_file, "a", encoding='utf-8') as f:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"FAILED_PASSWORD_ATTEMPT {now}\n")
    except Exception as e:
        print("Error recording failed attempt:", e)


def check_failed_attempt():
    try:
        with open(dear_diary_file, "r", encoding='utf-8') as f:
            lines = f.readlines()

        failed_attempts = [line for line in lines if line.startswith("FAILED_PASSWORD_ATTEMPT")]
        if failed_attempts:
            # Remove all failed attempt lines
            lines = [line for line in lines if not line.startswith("FAILED_PASSWORD_ATTEMPT")]
            with open(dear_diary_file, "w", encoding='utf-8') as f:
                f.writelines(lines)

            # Return the datetime string of the most recent failed attempt (strip prefix)
            last_attempt = failed_attempts[-1].strip().split(" ", 1)[1]
            return last_attempt
    except FileNotFoundError:
        return None
    except Exception as e:
        print("Error checking failed attempts:", e)
    return None


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
            rainbow_print("🔒Your Secrets Are Safe With Me. Bye!🔒")
            exit()
        else:
            rainbow_print("Invalid option. Please try again.")
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
                    date = valid_date.strftime("%Y-%m-%d")  # normalizes the format
                    break
                except ValueError:
                    red_print("Invalid date format. Please enter the date like 2025-05-31 or press Enter to add system's date.")
        
        entry = input("Write your diary entry:\n")
        with open(dear_diary_file, "a", encoding='utf-8') as f:
            f.write(f"--- {date} ---\n{entry}\n\n")
        rainbow_print("Entry added successfully!")
    except Exception as e:
        red_print("Failed to write entry:", e)

def read_latest_entry():
    try:
        with open(dear_diary_file, "r", encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                rainbow_print("📝 No diary entries yet.")
                return
            entries = content.split("\n\n")
            rainbow_print("🕑 Latest Entry:\n" + entries[-1])
    except FileNotFoundError:
        red_print("Diary file not found.")
    except Exception as e:
        red_print("Failed to read latest entry:", e)

# 
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

# 
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
    PASSWORD = "123"
    attempt = input("Enter super secret password: ")
    if attempt == PASSWORD:
        return True
    else:
        record_failed_attempt()
        print("That is not the super secret password!")
        return False

if check_password():
    # If the passwoord is correct, it runs the rest of the program.
    dear_diary_exists()
    main_menu()
else:
    # says that it sends a message just to panic secret stealer XD
    rainbow_print("My secrets are safe from you!!! Sending message of failed attempt to owner!")
    exit()


check_password()



