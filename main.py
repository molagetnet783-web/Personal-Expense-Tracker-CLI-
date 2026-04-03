from tracker_logic import add_expense, show_monthly_total
from colorama import init, Fore

init(autoreset=True)

def main():
    while True:
        print(Fore.CYAN + "\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. Show Monthly Total")
        print("3. Exit")

        choice = input(Fore.YELLOW + "Enter your choice: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category (Food/Rent/Fun): ")
                add_expense(amount, category)
                print(Fore.GREEN + "Expense added successfully!")
            except ValueError:
                print(Fore.RED + "Invalid amount entered.")

        elif choice == '2':
            total = show_monthly_total()
            print(Fore.GREEN + f"Total expenses this month: {total}")

        elif choice == '3':
            print(Fore.BLUE + "Goodbye!")
            break

        else:
            print(Fore.RED + "Invalid choice. Try again.")

if __name__ == "__main__":
    main()

