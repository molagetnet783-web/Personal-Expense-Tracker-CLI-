import csv
import os
from datetime import datetime

FILE_PATH = os.path.join('data', 'expenses.csv')

# Ensure data folder exists
os.makedirs('data', exist_ok=True)

# Ensure file exists with header
if not os.path.isfile(FILE_PATH):
    with open(FILE_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "amount", "category"])


def add_expense(amount, category):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_PATH, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, amount, category])


def show_monthly_total():
    total = 0
    current_month = datetime.now().strftime("%Y-%m")

    with open(FILE_PATH, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['timestamp'].startswith(current_month):
                total += float(row['amount'])

    return total

