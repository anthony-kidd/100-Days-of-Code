"""
Name: tip-calculator.py
Author: Anthony Kidd
Purpose: This program will calculate the tip ammount for a bill
12-17-2024 - File created & base prgram began
"""

#* Function to collect the bill ammount, tip percentage, and if the person wants to split the bill.
def collectBillInfo(): 
    """ This is a function to collect and validate the bill total before tip."""
    bill_ammount = input("Please enter the bill ammout.\n$")
    bill_ammount =float(bill_ammount)
    return bill_ammount

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
            # Validation loop for custom tip percentage
            while True:
                tip_percent = input("What percentage tip would you like to leave?\n")
                try: tip_percent = float(tip_percent)
                except: TypeError
                if isinstance(tip_percent, float):
                    break

                else:
                    print("Error: Invalid input!")
            break
        else:
            print("Error: Invalid choice!")
    return tip_percent

def collectSplittingInfo():
    """ This function allows the user to choose if the bill will be split and how many people it will be split with."""
    # Validation loop for split bill option
    while True:
        split_bill = input("Do you want to split the bill with others?\n\t1. Yes\n\t2. No\n")
        if split_bill == "1":
            split_bill = True
            break
        elif split_bill == "2":
            split_bill = False
            break
        else:
            print("Error: Invalid choice!")

    # Validation loop for number of people splitting bill
    while True:
        if split_bill == True:
            number_of_people = input("Please enter the number of people to split the bill between.\n")
            try: number_of_people = int(number_of_people)
            except: TypeError
            if isinstance(number_of_people, int):
                break
            else:
                print("Error: Invalid input!")
        else:
            number_of_people = 1
            break
    return split_bill, number_of_people

def calculateTip(bill_ammount, tip_percent):
    tip = bill_ammount * tip_percent/100
    print(tip)

def main():
    bill_ammount = collectBillInfo()
    tip_percent = collectTipInfo()
    split_bill, number_of_people = collectSplittingInfo()
    calculateTip(bill_ammount, tip_percent)

main()
