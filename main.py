# Smart Budget & Expense Tracker

budget = float(input("Enter your total budget: "))
expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    expenses.append((name, amount))
    print(f"Expense '{name}' added successfully!")

def view_expenses():
    print("\n--- Your Expenses ---")
    
    if len(expenses) == 0:
        print("No expenses added yet.")
        return

    total_spent = 0
    for name, amount in expenses:
        print(f"{name} - ₹{amount}")
        total_spent += amount

    print("\nTotal Spent =", total_spent)
    print("Budget Left =", budget - total_spent)

while True:
    print("\nSelect an option:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        print("Program ended.")
        break
    else:
        print("Invalid choice. Try again.")