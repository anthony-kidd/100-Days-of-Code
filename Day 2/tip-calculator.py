"""
Name: tip-calculator.py
Author: Anthony Kidd
Purpose: This program will calculate the tip ammount for a bill
12-17-2024 - File created & base prgram began
12-19-2024 - Sipmlified functions, removed split_bill boolean, defined functions for printing error messages, 
             defined custom tip function to avoid deep encapsulation, renamed and completed the calculateBill function
"""
def inputError():
    """ Function to print errors for invalid inputs"""
    print("Error: Invalid input!")

def ChoiceError():
    """ Function to print errors for invalid choices"""
    print("Error: Invalid choice!")

def collectBillInfo(): 
    """ This is a function to collect and validate the bill total before tip."""
    while True:
        bill_ammount = input("Please enter the bill ammout.\n$")
        try: bill_ammount =float(bill_ammount)
        except: TypeError
        if isinstance(bill_ammount, float):
            return bill_ammount
            break
        else:
            inputError()

def customTip():
    """ Function to define a custom tip ammount """
    while True:
        tip_percent = input("What percentage tip would you like to leave?\n")
        try: tip_percent = float(tip_percent)
        except: TypeError
        if isinstance(tip_percent, float):
            break
        else:
            inputError()
        break
    return tip_percent

def collectTipInfo():
    """ This function allows the user to select the percentage they would like to leave as a tip."""
    # Validation loop to ensure the tip ammount is properly selected
    while True:
        tip_ammount_selection = input("Please enter the corresponding number for the desiered tip percentage:\n\t1. 10%\n\t2. 15%\n\t3. 20%\n\t4. Costom\n")
        if tip_ammount_selection == "1":
            tip_percent = 10.0
            break
        elif tip_ammount_selection == "2":
            tip_percent = 15.0
            break
        elif tip_ammount_selection == "3":
            tip_percent = 20.0
            break
        elif tip_ammount_selection == "4":
            tip_percent = customTip()
            break
        else:
            ChoiceError()
    return tip_percent

def splitBill():
    """ This function allows the user to choose if the bill will be split and how many people it will be split with."""
    while True:
        number_of_people = input("Please enter the number of people to split the bill between.\nif you do not wish to split, please enter '1'\n")
        try: number_of_people = int(number_of_people)
        except: TypeError
        if isinstance(number_of_people, int):
            break
        else:
            inputError()
    return number_of_people

def calculateBill(bill_ammount, tip_percent, number_of_people):
    """ This function will calculate the total of the bill including tip."""
    tip = bill_ammount * tip_percent/100
    total = bill_ammount + tip
    if number_of_people > 1:
        total = bill_ammount + tip
        tip_per_person = tip / number_of_people
        bill_per_person = bill_ammount /number_of_people
        total_per_person = total / number_of_people
        print(f"Bill total after tip: ${total}")
        print(f"Bill per person ${bill_per_person}")
        print(f"Tip per person: ${tip_per_person}")
        print(f"Total ammount owed per person (bill and tip) ${total_per_person}")
    else:
        print(f"Bill total before tip: ${bill_ammount}")
        print(f"Tip: ${tip}")
        print(f"Bill total after tip: ${total}")
    
    

def main():
    """ Main function to run program"""
    bill_ammount = collectBillInfo()
    tip_percent = collectTipInfo()
    number_of_people = splitBill()
    calculateBill(bill_ammount, tip_percent, number_of_people)

main() # Calling main function
