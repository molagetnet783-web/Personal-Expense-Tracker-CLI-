A simple command-line Personal Expense Tracker built with Python. It allows users to log daily expenses, categorize them, and view a monthly total. Data is stored in a CSV file for easy access and portability.

## Features
- Add daily expenses with amount and category
- Automatic timestamp for each entry
- Categories: Food, Rent, Fun (extendable)
- Monthly total calculation
- Clean CLI with colored prompts (using `colorama`)
- CSV-based storage (`data/expenses.csv`)

## Project Structure
```
 
├── main.py              # CLI interface
├── tracker_logic.py     # Core logic (file handling, calculations)
├── data/
│   └── expenses.csv     # Stored expense data (auto-created)
└── requirements.txt     # Dependencies
```

## Installation
1. Clone or download the project.
2. Navigate to the project folder:
   ```bash
   cd expense_tracker
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the application using:
```bash
python main.py
```

### Menu Options
- **1. Add Expense** → Enter amount and category
- **2. Show Monthly Total** → Displays total spending for current month
- **3. Exit** → Close the program

## Data Storage
- Expenses are stored in: `data/expenses.csv`
- Format:
  ```
  timestamp,amount,category
  2026-04-03 10:30:00,50,Food
  ```

## Example
```
=== Personal Expense Tracker ===
1. Add Expense
2. Show Monthly Total
3. Exit

Enter your choice: 1
Enter amount: 100
Enter category: Food
Expense added successfully!
```

## Future Improvements
- Category-wise summaries
- Date range filtering
- Data visualization (charts)
- Budget limits and alerts
- Export reports (Excel/PDF)

## Requirements
- Python 3.x
- colorama

 
