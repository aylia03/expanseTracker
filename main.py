from expenses import add_expenses, view_expenses, calculate_total
from storage import *

expenses = [] # list python

def main():

    load_expenses_from_csv(expenses)

    while True:
        print("************************************************************")
        print("Expanse Tracker")
        print("************************************************************")
        print("What do you want to do?")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Spending")
        print("4. Export Expenses to CSV")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            export_to_csv(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()





