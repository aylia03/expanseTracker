import datetime

expenses = [] # list python

"""
    add new expenses to the list 

    Parameters:
    amount (int) 
    category (str) 
    description (str) 
    date_input (today)

    """


def add_expenses():
    try:
        amount = int(input("How many expenses? "))
        category = input("What category do you want to add? (e.g., Food, Transport, etc. ")
        description = input("What do you want to add?")
        date_input = input(f"Enter date (YYYY-MM-DD) or press Enter for today: ")

        if not date_input:
            date_input = datetime.date.today()

        expense = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date_input
        }
        expenses.append(expense)

        print("Expenses added successfully")

    except ValueError:
        print("Invalid input, try again")


"""
    display expenses 
    Parameters:
    expenses (list) 

    """


def view_expenses():
    if len(expenses) == 0:
        print("No expenses to show")
        return

    print("\n--- Expense List ---")
    idx = 1
    for expense in expenses:
        print(f"{idx}. ${expense['amount']} - {expense['category']} - {expense['description']} ({expense['date']})")
        idx += 1


def calculate_total():
    sum = 0
    for expense in expenses:
        sum += expense['amount']
    print(f"Total: {sum}")

def welcome():
    print("************************************************************")
    print("Expanse Tracker")
    print("************************************************************")
    print("What do you want to do?")
    print("add Expenses (A), view expenses (B), calculate total (C) and Quite (Q)")
    print("************************************************************")

def menu():
    while True:
        try:
            userInput = input("Type A, B, C or Q ").upper()

            if userInput not in ["A", "B", "C", "Q", "y", "n"]:
                raise ValueError("Invalid input, try again")

            if userInput == "A":
                add_expenses()
            elif userInput == "B":
                view_expenses()
            elif userInput == "C":
                calculate_total()
            elif userInput == "Q":
                print("Quit")

            restart = input("Do you want to make another input? (y/n): ").lower()
            if restart == 'n':
                print("Exiting the program.")
                break


        except ValueError as e:
            print(e)


welcome()
menu()





