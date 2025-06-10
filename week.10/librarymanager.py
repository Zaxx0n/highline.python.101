#!/usr/bin/env python3
# Assignment: Week 10 - Personal Library Management System
# Author: Zachary Derrick
# Github: https://github.com/Zaxx0n?tab=repositories                    
# Date of latest revision:  6/09/2025   
# Purpose: create a Python program that acts as a personal library manager. Users should be able to manage 
#          their collection of books, recording important information like title, author, publication year, 
#          and their personal rating. Your program will utilize file operations to save and retrieve book information, 
#          so users can maintain their library across sessions.
# Resources: Final Project Word File - OpenAI - deardiary.py (can be found on my github) 
#            
# Notes: This program acts as a personal library manager, allowing users to add, search, update, 
#        and remove books from their collection. I used OpenAI's assistance to work out the JSON 
#        file handling for saving and loading book data across sessions, which helped simplify 
#        data persistence 
# 
#        I wanted to make the interface visually engaging, so I experimented with ANSI escape codes 
#        for colorful text output throughout the program. This adds personality and helps guide 
#        the user with color-coded messages .
#
#        The book rating system uses "Aura", letting users rate 
#        books on a 1-5 scale displayed with a glowing emoji 🔆
#        
#        The program organizes books by author last name and  searching by title or author.
#        Input validation and confirmation loops ensure data correctness and improve the user experience.
#        
#        An easy future enhancement could be adding user profiles to manage multiple libraries 
#        or a graphical interface.  I played a bit with graphical interface, but it was taking 
#        too much time, so I just went back to my original code.
#  

# modules

import json # json allows for organized data storage
import os
import random

library_file = "codex.json"

def load_library():
    try:
        with open("codex.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        red_print("⚠ Error: codex.json is corrupted.")
        return []
    
# we need to load the library from the start
library = load_library()  

quotes = []

quotes_file = "quotes.json"

def red_print(text):
    bright_red = "\033[91m"
    reset = "\033[0m"
    print(f"{bright_red}{text}{reset}")

def calming_print(text):
    soft_blue = "\033[96m"
    reset = "\033[0m"
    print(f"{soft_blue}{text}{reset}")

def color_text(text, color_code):
    reset = "\033[0m"
    return f"\033[{color_code}m{text}{reset}"

def load_quotes():
    global quotes
    if os.path.exists(quotes_file):
        with open(quotes_file, "r", encoding="utf-8") as f:
            quotes = json.load(f)

def random_quote():
    if quotes:
        return random.choice(quotes)
    else:
        return "Be well!"
    
def save_library():
    with open(library_file, 'w') as file:
        json.dump(library, file, indent=4)

def codex_banner():
    total_width = 60
    left_emojis = "📕📙📗📘"
    right_emojis = "📘📗📙📕"
    
    # alignment took some figuring out so this is what I ended on
    # estimate that each emoji takes 2 character spaces, 8 emojis × 2 = 16
    emoji_width = len(left_emojis + right_emojis) * 2 
    title = "The Codex"
    inner_space = total_width - emoji_width

    # banner lines
    title_line = f"{left_emojis}{title.center(inner_space)}{right_emojis}"
    banner_line = "──────────── ⋆⋅☆⋅⋆ ────────────".center(total_width)

    print(title_line)
    print(banner_line)

def codex_has_books():
    if not library:
        red_print("\n╭⚠ NOTICE ⚠╮\n│ The Codex is empty. Please add a book first.\n")
        input("\nPress Enter to return to the main menu...↩️\n")
        return False
    return True

def add_book():
    if not codex_has_books():
        return
    print("\nAdd a Book to The Codex")

    # asks for initial input first
    title = input("Title: ")
    last_name = input("Author's Last Name: ")
    first_name = input("Author's First Name: ")
    aura = input("Aura (1-5): ")

    # confirmation loop
    while True:
        author = f"{last_name}, {first_name}"
        print("\n:: Please confirm the book's details ::")
        print(f"   > Title  : {title}")
        print(f"   > Author : {author}")
        print(f"   > Aura   : 🔆 {aura}")

        confirm = input("\nAre all details correct? (y/n): ").lower()
        if confirm == 'y':
            break
        # uses a menu for input validation
        elif confirm == 'n':
            print("\nWhich would you like to change?")
            print("  1) Title")
            print("  2) Author's Last Name")
            print("  3) Author's First Name")
            print("  4) Aura")
            print("  5) Start over")
            choice = input("> ")
            if choice == '1':
                title = input("New Title: ")
            elif choice == '2':
                last_name = input("New Last Name: ")
            elif choice == '3':
                first_name = input("New First Name: ")
            elif choice == '4':
                aura = input("New Aura: ")
            elif choice == '5':
                title = input("Title: ")
                last_name = input("Author's Last Name: ")
                first_name = input("Author's First Name: ")
                aura = input("Aura (1-5): ")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    # saves the confirmed book
    author = f"{last_name}, {first_name}"
    book = {"title": title, "author": author, "aura": aura}
    library.append(book)
    save_library()
    print(f"\n'{title}' by {author} added to The Codex!\n")



def list_all_books():
    if not codex_has_books():
        return
    print(color_text(" ⋆⋅☆⋅⋆  The Codex — Sorted by Author  ⋆⋅☆⋅⋆\n","97"))
    print(color_text("  Format: Last, First\t | Title |   Aura\n", "36"))
    
    # Sort by last name (which comes first in your 'author' string)
    library_sorted = sorted(library, key=lambda book: book["author"].split(",")[0].strip().lower())
    
    for index, book in enumerate(library_sorted, start=1):
        print(f"  {index}) {book['author']:<25} \"{book['title']}\"{'.' * (32 - len(book['title']))} 🔆 {book['aura']:>2}")


    input("\n\tPress Enter to return to the main menu...↩️\n ")


def search_books():
    if not codex_has_books():
        return
    print("\nSearch for Book by Title or Author")
    
    while True:
        search = input("Enter a word from the title or author (or 'q' to return to the main menu): ").lower()
        if search == 'q':
            return
        
        matches = [book for book in library if search in book["title"].lower() or search in book["author"].lower()]
        
        if matches:
            print("\n╭───────────────╮")
            print("│ Matches Found │")
            print("╰───────────────╯\n")
            for i, book in enumerate(matches, 1):
                print(f"  {i}) '{book['title']}' by {book['author']} - 🔆 {book['aura']}")
            choice = input("\nPress Enter to return to the main menu, or type 's' to search again: ").lower()
            if choice == 's':
                continue  # loops back to search again
            else:
                return  # exit to main menu
        else:
            red_print("\n╭⚠ NOTICE ⚠╮\n│ No books found matching that search. Try again or type 'q' to return.")

# change the book aura :P
def update_rating():
    if not codex_has_books():
        return
    print("\n🔆 Update a Book's Aura")

    while True:
        search_term = input("Enter a word from the title or author (or 'q' to cancel): ").lower()
        if search_term == 'q':
            red_print("Update cancelled.\n")
            return

        # finds matches by title or author
        matches = [book for book in library if search_term in book["title"].lower() or search_term in book["author"].lower()]

        if not matches:
            print("No books found matching that search. Try again or enter 'q' to cancel.")
        else:
            break

    # returns the matches found
    print("\nMatching books:")
    for i, book in enumerate(matches, start=1):
        print(f"  {i}) '{book['title']}' by {book['author']} - 🔆 {book['aura']}")

    while True:
        choice = input("Enter the number of the book to update the aura (or 'q' to cancel): ")
        if choice.lower() == 'q':
            red_print("Update cancelled.\n")
            return
        if choice.isdigit() and 1 <= int(choice) <= len(matches):
            selected_book = matches[int(choice) - 1]
            break
        else:
            red_print("Invalid choice, please try again.")

    new_rating = input(f"Enter new aura for '{selected_book['title']}': ")
    selected_book["aura"] = new_rating
    save_library()
    print(f"Aura for '{selected_book['title']}' updated to 🔆 {new_rating}")


# here we have the functionality to remove books, a stretch goal would be to list all books and choose from that
# possibly with some sorting fuctionality 
def remove_book():
    if not codex_has_books():
        return
    print("\nRemove a Book from The Codex")

    while True:
        search_term = input("Enter part of the title or author to search (or 'q' to cancel): ").lower()
        if search_term == 'q':
            red_print("\n╭───────────╮\n│   X   Cancelled - Returning to The Codex Menu")
            return

        matches = [book for book in library if search_term in book["title"].lower() or search_term in book["author"].lower()]
        
        if not matches:
            red_print("\n╭⚠ NOTICE ⚠╮\n│ No matching books found. Try again.")
            continue

        print("\nMatching books:")
        for i, book in enumerate(matches, start=1):
            print(f"  {i}) '{book['title']}' by {book['author']} - 🔆 {book['aura']}")

        choice = input("Enter the number of the book to remove (or 'q' to cancel): ")
        if choice.lower() == 'q':
            red_print("\n╭───────────╮\n│   X   Cancelled. Returning to The Codex menu.\n")
            return
        if choice.isdigit() and 1 <= int(choice) <= len(matches):
            selected_book = matches[int(choice) - 1]
            library.remove(selected_book)
            save_library()
            print(f"\n╭───────────╮\n│   ✓   '{selected_book['title']}' removed from The Codex.\n")
            return
        else:
            red_print("\n╭⚠ NOTICE ⚠╮\n│ Invalid choice. Try again.")


def main_menu():
    load_library()
    load_quotes()
    
    while True:
        codex_banner()
        print("    1) " + color_text("[BOOK]", "94") + "\tAdd a Book")      # Bright Blue
        print("    2) " + color_text("||||||", "96") + "\tList All Books")  # Bright Cyan
        print("    3) " + color_text("<<S>>", "92") + "\tSearch for Book by Title or Author")  # Bright Green
        print("    4) " + color_text("*** **", "93") + "\tUpdate a Book's Aura")  # Bright Yellow
        print("    5) " + color_text("(X X)", "91") + "\tRemove a Book from the Codex")  # Bright Red
        print("    6) " + color_text("[EXIT]", "95") + "\tQuit Program\n")   # Bright Magenta
        
        selected_main_option = input("> ")
        if selected_main_option == '1':
            add_book()
        elif selected_main_option == '2':
            list_all_books()
        elif selected_main_option == '3':
            search_books()
        elif selected_main_option == '4':
            update_rating()
        elif selected_main_option == '5':
            remove_book()
        elif selected_main_option == '6':
            calming_print(random_quote())
            exit()
        else:
            red_print("\n╭⚠ NOTICE ⚠╮\n│Invalid choice. Try again.")

main_menu()