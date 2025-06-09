#!/usr/bin/env python3
# Assignment: Week 10 - Personal Library Management System
# Author: Zachary Derrick                    
# Date of latest revision:  6/09/2025   
# Purpose: create a Python program that acts as a personal library manager. Users should be able to manage 
#          their collection of books, recording important information like title, author, publication year, 
#          and their personal rating. Your program will utilize file operations to save and retrieve book information, 
#          so users can maintain their library across sessions.
# Resources: Final Project Word File - OpenAI -  
#            
# Notes:  

# modules
# json allows for organized data storage
import json 
import os
import random

library_file = "codex.json"
library = []
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

def load_library():
    global library
    if os.path.exists(library_file):
        with open(library_file, 'r') as file:
            library = json.load(file)
            print("Codex Loaded")
    else:
        library = []

def save_library():
    with open(library_file, 'w') as file:
        json.dump(library, file, indent=4)

def codex_banner():
    total_width = 60
    left_emojis = "📕📙📗📘"
    right_emojis = "📘📗📙📕"
    
    # Estimate that each emoji takes 2 character spaces
    emoji_width = len(left_emojis + right_emojis) * 2  # 8 emojis × 2 = 16
    title = "The Codex"
    inner_space = total_width - emoji_width

    # Build banner lines
    title_line = f"{left_emojis}{title.center(inner_space)}{right_emojis}"
    stars_line = "──────────── ⋆⋅☆⋅⋆ ────────────".center(total_width)

    print(title_line)
    print(stars_line)



def add_book():
    while True:
        # starts fresh or after "start over"
        title = input("\n📖 Title: ")
        last_name = input("Author's Last Name: ")
        first_name = input("Author's First and Middle Name(s): ")
        aura = input("Aura (1-5): ")

        while True:
            author = f"{last_name}, {first_name}"
            print("\n🧾 Please confirm the details:")
            print(f"  📖 Title: {title}")
            print(f"  ✍️ Author: {author}")
            print(f"  🔆 Aura: {aura}")
            confirm = input("Are all details correct? (y/n): ").lower()

            if confirm == 'y':
                book = {"title": title, "author": author, "aura": aura}
                library.append(book)
                save_library()
                print(f"\n✅ '{title}' by {author} added to The Codex!")
                
                # asks to add another
                again = input("Would you like to add another book? (y/n): ").lower()
                if again == 'y':
                    break  # break inner loop and restart add_book
                else:
                    return  # return to main menu

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
                    last_name = input("New Author's Last Name: ")
                elif choice == '3':
                    first_name = input("New Author's First Name: ")
                elif choice == '4':
                    aura = input("New Aura (1-5): ")
                elif choice == '5':
                    break  # start over completely
                else:
                    red_print("Invalid selection. Try again.")
            else:
                print("Please enter 'y' or 'n'.")


def list_all_books():
    print("\nAll Books in The Codex:")
    if not library:
        print("🧿(Your Codex is Empty!)🧿")
    for index, book in enumerate(library, start=1):
        print(f"  {index}) '{book['title']}' by {book['author']} - 🔆 {book['aura']}")

def search_books():
    print("\n🔍 Search for Book by Title or Author")
    
    while True:
        search = input("Enter a word from the title or author (or 'q' to return to the main menu): ").lower()
        if search == 'q':
            return
        
        matches = [book for book in library if search in book["title"].lower() or search in book["author"].lower()]
        
        if matches:
            print("\n📚 Matches found:")
            for i, book in enumerate(matches, 1):
                print(f"  {i}) '{book['title']}' by {book['author']} - ⭐ {book['aura']}")
            break
        else:
            red_print("❌ No books found matching that search. Try again or type 'q' to return.")



def update_rating():
    print("\n🔆 Update a Book's Aura")
    search_term = input("Enter a word from the title or author: ").lower()

    # Find matches by title or author
    matches = [book for book in library if search_term in book["title"].lower() or search_term in book["author"].lower()]

    if not matches:
        print("No books found matching that search.")
        return

    # List matching books
    print("\nMatching books:")
    for i, book in enumerate(matches, start=1):
        print(f"  {i}) '{book['title']}' by {book['author']} - 🔆 {book['aura']}")

    # Let user select which book to update
    while True:
        choice = input("Enter the number of the book to update the aura (or 'q' to cancel): ")
        if choice.lower() == 'q':
            print("Update cancelled.")
            return
        if choice.isdigit() and 1 <= int(choice) <= len(matches):
            selected_book = matches[int(choice) - 1]
            break
        else:
            red_print("Invalid choice, please try again.")

    # Get new rating
    new_rating = input(f"Enter new aura for '{selected_book['title']}': ")
    selected_book["aura"] = new_rating
    save_library()
    print(f"Codex Aura updated to 🔆 {new_rating}")

def remove_book():
    print("\n🕯️ Remove a Book from The Codex")

    while True:
        search_term = input("Enter part of the title to search (or 'q' to cancel): ").lower()
        if search_term == 'q':
            print("❎ Cancelled. Returning to the Codex menu.")
            return

        matches = [book for book in library if search_term in book["title"].lower()]
        
        if not matches:
            red_print("❌ No matching books found. Try again.")
            continue

        print("\nMatching books:")
        for i, book in enumerate(matches, start=1):
            print(f"  {i}) '{book['title']}' by {book['author']} - 🔆 {book['rating']}")

        choice = input("Enter the number of the book to remove (or 'q' to cancel): ")
        if choice.lower() == 'q':
            print("❎ Cancelled. Returning to the Codex menu.")
            return
        if choice.isdigit() and 1 <= int(choice) <= len(matches):
            selected_book = matches[int(choice) - 1]
            library.remove(selected_book)
            save_library()
            print(f"✅ '{selected_book['title']}' removed from The Codex.")
            return
        else:
            red_print("⚠️ Invalid choice. Try again.")



def main_menu():
    load_library()
    load_quotes()
    codex_banner()
    while True:
        print("\nMake a Selection from Below:")
        print("    1) 🪄 Add a Book")
        print("    2) 📚 List All Books")
        print("    3) 🔭 Search for Book by Title or Author")
        print("    4) 🔆 Update a Book's Aura")
        print("    5) 🕯️ Remove a Book from the Codex")
        print("    6) 🌙 Quit Program\n")
        
        selected_main_option = input("> ")
        (f"You have selected option:{selected_main_option}")
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
            red_print("That is not an option. Please select again.")

main_menu()