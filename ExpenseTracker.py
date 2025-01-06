def main():
    expenses = []  # List to store expenses

    print("Welcome to the Interactive Expense Tracker!")
    while True:
        print("\nChoose an option:")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Calculate total expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            calculate_total(expenses)
        elif choice == '4':
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def add_expense(expenses):
    description = input("Enter a description for the expense: ")
    try:
        amount = float(input("Enter the amount: "))
        expenses.append((description, amount))
        print(f"Added expense: {description} - ${amount:.2f}")
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
    else:
        print("\nExpenses:")
        for i, (description, amount) in enumerate(expenses, start=1):
            print(f"{i}. {description}: ${amount:.2f}")

def calculate_total(expenses):
    total = sum(amount for _, amount in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")

if __name__ == "__main__":
    main()
