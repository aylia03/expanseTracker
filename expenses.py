import datetime

"""
    add new expenses to the list 

    Parameters:
    amount (int) 
    category (str) 
    description (str) 
    date_input (today)

    """


def add_expenses(expenses):
    try:
        amount = int(input("How many expenses? "))
        category = input("What category do you want to add? (e.g., Food, Transport, etc.) ")
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


def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses to show")
        return

    print("\n--- Expense List ---")
    idx = 1
    for expense in expenses:
        print(f"{idx}. ${expense['amount']} - {expense['category']} - {expense['description']} ({expense['date']})")
        idx += 1


def calculate_total(expenses):
    sum = 0
    for expense in expenses:
        sum += expense['amount']
    print(f"Total: {sum}")