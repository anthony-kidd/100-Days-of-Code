"""
Name: check-even-or-odd.py
Author: Anthony Kidd
Purpose: This program will check if a number is even or odd.
12-22-2024 - File created & base program completed.
"""
def checkEven(number):
    """ This function checks if the number is even or odd."""
    if number % 2 == 0:
        print(f"{number} is even!")
    else:
        print(f"{number} is odd!")

def validateNumber(number_string):
    """ This function validates the string is an integer."""
    while True:
        if number_string == "ZZZ":
            print("Exiting program...")
            exit(0)
        else:
            try: number_string = int(number_string)
            except: TypeError
            if isinstance(number_string, int):
                return number_string
                break
            else:
                number_string = input("Error: please enter a valid integer or 'ZZZ' to exit: ")

def main():
    """ The main function continues accepting input from the user until they type 'ZZZ' to exit the program."""
    while True:
        number_string = input("Please enter a number to check if it is even or odd or 'ZZZ' to exit: ")
        number = validateNumber(number_string)
        checkEven(number)
    
main()
