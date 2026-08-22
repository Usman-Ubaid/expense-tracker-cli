# Expense Tracker CLI

A simple command-line tool to track your personal expenses, built with Python's standard library (`argparse` + `csv`). No external dependencies required.

This project follows the [Expense Tracker](https://roadmap.sh/projects/expense-tracker) challenge from [roadmap.sh](https://roadmap.sh).

## Features

- Add an expense with a description, amount, and category
- List all expenses, optionally filtered by category
- Update an existing expense
- Delete an expense
- View a summary of total spending, optionally filtered by month

## Requirements

- Python 3.8+
- No external packages — everything used is from the standard library

## Setup

```bash
git clone <your-repo-url>
cd expense-tracker
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

## Usage

### Add an expense

```bash
python expense_tracker.py add --description "Lunch" --amount 20 --category Food
```

### List expenses

```bash
python expense_tracker.py list
```

Filter by category:

```bash
python expense_tracker.py list --category Food
```

### Update an expense

```bash
python expense_tracker.py update --expense_id 1 --amount 25
```

Only the fields you provide are updated — everything else stays the same.

### Delete an expense

```bash
python expense_tracker.py delete --expense_id 1
```

### View summary

Total spending across all expenses:

```bash
python expense_tracker.py summary
```

Total spending for a specific month:

```bash
python expense_tracker.py summary --month 2026-08
```

## How data is stored

Expenses are stored locally in `expenses.csv` in the project directory, with the following columns:

| Column        | Description                          |
|---------------|---------------------------------------|
| `id`          | Unique, auto-incrementing expense ID   |
| `date`        | Date the expense was added (`YYYY-MM-DD`) |
| `description` | Short description of the expense      |
| `amount`      | Expense amount                        |
| `category`    | Expense category (e.g. Food, Transport) |

`expenses.csv` is created automatically the first time you add an expense, and is excluded from version control via `.gitignore`.

## Project structure

```
expense-tracker/
├── expense_tracker.py   # Main CLI script
├── expenses.csv          # Generated automatically (not committed)
├── .gitignore
└── README.md
```
