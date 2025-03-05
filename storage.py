import csv

def export_to_csv(expenses, filename="expenses.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["amount", "category", "description", "date"])
        writer.writeheader()
        writer.writerows(expenses)
    print(f"Expenses saved to {filename}")

def load_expenses_from_csv(expenses, filename="expenses.csv"):
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])  # Convert amount back to float
                expenses.append(row)
    except FileNotFoundError:
        print("No saved expenses found. Starting fresh.")
