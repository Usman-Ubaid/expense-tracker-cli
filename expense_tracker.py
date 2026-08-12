import argparse;
import csv;
import os;

CSV_FILE = "expenses.csv"
FIELD_NAMES = ['id', 'date','description','amount','category']

def load_expenses():
    """Read all expenses from the CSV file into a list of dicts"""
    if not os.path.exists(CSV_FILE):
        return []
    with open(CSV_FILE, "r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def save_expense(expenses):
    """Write the full list of expenses into the CSV file"""
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELD_NAMES)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(description, amount, category):
    # TODO
    pass

def list_expense(category):
    # TODO
    pass

def update_expense(expense_id, description=None, amount=None, category=None):
    # TODO
    pass

def delete_expense(expense_id):
    # TODO
    pass

def summary(month=None):
    # TODO
    pass

def main():
    parser = argparse.ArgumentParser(description="Simple Expense Tracker")
    subparsers = parser.add_subparsers(dest="command")

     # TODO: define subparsers for add, list, delete, update, summary

    args = parser.parse_args()

    # TODO: dispatch to the right function based on args.command

if __name__== "__main__":
    main()