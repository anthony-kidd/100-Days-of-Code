"""
Name: create-folders.py
Author: Anthony Kidd
Purpose: This program will create a group of folders for my 100 days of 
         code challenge in the current directory using a for loop.
GitHub Repo for createFolder function: https://gist.github.com/keithweaver/562d3caa8650eefe7f84fa074e9ca949
Revision History:
12-16-2024 - File created & base program completed.
12-17-2024 - Corrected typos in validateFolderName() error output message
"""
# *Necessary Imports
import os

# *Function to create folders
def createFolder(directory): # This function was developed by Kieth Weaver. Source in header.
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        exit(1) # Added by Anthony Kidd 12-16-2024

# *Function to validate folder names
def validateFolderName(folder_name):
    while True:
        if folder_name.isalnum(): # Validating the name is only comprised of alpha numeric characters
            break
        else:
            print("Error: number of folders is not recognized as alpha numeric. please try again.")
            folder_name = str(input("Please enter the name for the folders: "))
    return folder_name

# *Function to validate the number of folders
def validateNumberofFolders(number_of_folders):
    while True:
        if number_of_folders.isdigit(): # Checking if number_of_folders is an integer
            number_of_folders = int(number_of_folders)
            break
        else:
            print("Error: number of folders is not recognized as an integer. please try again.")
            number_of_folders = (input("Please enter the number of folders to create: "))
    return int(number_of_folders)

# *Main function
def main():
    # Command Line User Interface
    print("\nCreate Folders.py\n")
    print("This program will create a user specified ammount of folders in the current working directory\n")
    folder_name = str(input("Please enter the name for the folders: "))
    folder_name = validateFolderName(folder_name)
    number_of_folders = (input("Please enter the number of folders to create: "))
    number_of_folders = validateNumberofFolders(number_of_folders) # Assign return value to variable

    # Using a for loop to create the necessary folders.        
    for i in range (number_of_folders):
        day = i + 1 # Since Python increments a for loop starting at 0, we must add 1 to get the correct number.
        createFolder(f'./{folder_name} {day}/')
        # This function creates a folder in the current directory called Day + the number of the day.

main()
