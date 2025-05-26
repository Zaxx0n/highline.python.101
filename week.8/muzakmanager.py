#!/usr/bin/env python3
# Assignment: Week 8 - The Music Playlist Manager
# Author: Zachary Derrick                    
# Date of latest revision:  5/25/2025   
# Purpose: create a simple music playlist manager using Python lists. 
#          add songs to a playlist, remove songs, view the playlist, 
#          and find out popular song choices
# Resources: A07 - Music Playlist Word Document, OpenAI - helped in making the loading previous playlist function. 
#            I also use OpenAI for quick emoji reference and suggestions.
# Notes: While playing around and researching the count() method, I found the collection module, which
#        is used especially for counting elements like the string names for our song titles.  
#        This program also saves a text file to the directory that the program is run from.  It also checks
#        text files in the directory for a header to recognize it as a playlist, skipping unreadable files.
#        A stretch goal for this would be to make a graphical interface, something I've only played around with.
#        Also, I'd probably add an option to seach through the playlist for a song being added and let the
#        user know if it already exists, but since part of the assignement is to count the most frequently added
#        song(s), I decided to not add this.

# modules
import os
from collections import Counter

global playlist_name

# this program uses multiple menus, this being the main menu
def main_menu():
    print("🎶\033[95mSuper Rad Music Manager 9000\033[0m🎶")
    while True:
        selected_main_option = input("""\nMake a Selection from Below:
                        1) 🆕 Create New Playlist
                        2) 📂 Open Previous Playlist
                        3) 👋 Quit Program     
                        \n""") 
        print("You have selected option:", selected_main_option)
        
        if selected_main_option == '1':
            create_new_playlist()
        elif selected_main_option == '2':
            open_playlist()
        elif selected_main_option == '3':
            print("Quitting Program, Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# function to create a new playlist: I added the if statement to remove .txt just incase someone typed itin the file name.
def create_new_playlist():   
    global playlist
    global playlist_name
    playlist = []
    playlist_name = input("Enter a name for your new playlist: ").strip()

    if playlist_name.lower().endswith('.txt'):
        playlist_name = playlist_name[:-4]

    print(f"New playlist '{playlist_name}' created.")
    playlist_menu()

# this was created so that playlists can be reopened and edited
def open_playlist():
    global playlist
    global playlist_name

    # this looks for the string '# SRMM9000' to make sure the file was created by this program and is a playlist
    # thus finding "valid_playlists"
    valid_playlists = []
    for f in os.listdir():
        if f.endswith('.txt'):
            try:
                with open(f, 'r') as file:
                    first_line = file.readline().strip()
                    if first_line == "# SRMM9000":
                        valid_playlists.append(f)
            except Exception:
                continue  
    #  prints the valid playlists for the user to choose from
    if valid_playlists:
        print("\nFound the following playlists:")
        for i, file in enumerate(valid_playlists, start=1):
            print(f"{i}) {file}")
        try:
            choice = int(input("Enter the number of the playlist to open: "))
            selected_file = valid_playlists[choice - 1]
        except (ValueError, IndexError):
            print("Invalid selection. Returning to main menu.")
            return
    # allows for importing of a playlist from a different directory
    else:
        selected_file = input("No valid playlists found.\nEnter the full path to the playlist file you'd like to use: ")

    try:
        with open(selected_file, 'r') as file:
            lines = file.readlines()
            if not lines or lines[0].strip() != "# SRMM9000":
                print("Invalid file format. Not a recognized playlist file.")
                return
            playlist = [line.strip() for line in lines[1:]] 
        playlist_name = os.path.splitext(os.path.basename(selected_file))[0]
        print(f"Playlist loaded from '{selected_file}'")
        playlist_menu()
    except FileNotFoundError:
        print("File not found. Returning to main menu.")


# I wanted users to be able to save their playlists to use again
def save_playlist():
    global playlist_name

    # Safety Check: makes sure that playlist_name has been given
    if not playlist_name:
        print("Error: No playlist name defined. Cannot save.")
        return

    filename = f"{playlist_name}.txt"
    try:
        with open(filename, 'w') as file:
            file.write("# SRMM9000\n")
            for song in playlist:
                file.write(f"{song}\n")
        print(f"Playlist saved to '{filename}'")
    except Exception as e:
        print(f"An error occurred while saving: {e}")

# the menu for editing playlists
def playlist_menu():
    while True:
        playlist_option = input("""\nWhat would you like to do?:
                        1) 🎶 Add Song to Playlist
                        2) ❌ Remove Song from Playlist
                        3) 📃 View Playlist     
                        4) 🔢 Display Number of Songs in Playlist
                        5) 🌟 Display Most Frequently Added Song
                        6) 💾 Save and Exit to Main Menu
                        7) 👋 Quit Program 
                        \n""") 
        print("You have selected option:", playlist_option)
        
        if playlist_option == '1':
            add_song()
        elif playlist_option == '2':
            remove_song()
        elif playlist_option == '3':
            view_playlist()
        elif playlist_option == '4':
            display_count()
        elif playlist_option == '5':
            display_most_frequent_song()
        elif playlist_option == '6':
            save_playlist()
            break
        elif playlist_option == '7':
            print("Quitting Program, Goodbye!")
            exit()
        else:
            print("Invalid option. Please try again.")

def add_song():
    song = input("Enter song title to add: ")
    playlist.append(song)
    print(f"'{song}' added to playlist.")

# this allows both the input of song name and a list to choose from for removal
def remove_song():
    if not playlist:
        print("Playlist is empty. Nothing to remove.")
        return

    removal = input("""\nHow would you like to remove a song?
                    1) Type the song title
                    2) Choose from a list
                    \nEnter option (1 or 2): """)

    if removal == '1':
        song = input("Enter the song title to remove: ")
        if song in playlist:
            playlist.remove(song)
            print(f"'{song}' removed from playlist.")
        else:
            print(f"'{song}' not found in playlist.")
    elif removal == '2':
        print("\nYour Playlist:")
        for count, song in enumerate(playlist, start=1):
            print(f"{count}. {song}")
        try:
            choice = int(input("Enter the number of the song to remove: "))
            removed_song = playlist.pop(choice - 1)
            print(f"'{removed_song}' removed from playlist.")
        except (ValueError, IndexError):
            print("Invalid selection. No song removed.")
    else:
        print("Invalid option. Returning to menu.")

def view_playlist():
    if playlist:
        print(f"\nPlaylist: {playlist_name}")
        for count, song in enumerate(playlist, start=1):
            print(f"{count}. {song}")
    else:
        print("Playlist is empty.")

def display_count():
    print(f"Total number of songs: {len(playlist)}")

def display_most_frequent_song():
    if not playlist:
        print("Playlist is empty.")
        return

    song_counts = Counter(playlist)
    if not song_counts:
        print("No songs to count.")
        return

    max_count = max(song_counts.values())
    most_common_songs = [song for song, count in song_counts.items() if count == max_count]

    print(f"\nMost frequently added song(s), added {max_count} time(s):")
    for song in most_common_songs:
        print(f"- {song}")


main_menu()
