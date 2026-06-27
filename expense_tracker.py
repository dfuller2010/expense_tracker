import json

FILENAME = "expenses.json"

def load_expenses():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(FILENAME, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    amount = float(input("Amount: "))
    category = input("Category: ")
    description = input("Description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added!")

def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    
    for i, expense in enumerate(expenses):
        amount = expense["amount"]
        category = expense["category"]
        description = expense["description"]
        print(f"{i + 1}. ${amount:.2f} | {category} | {description}")  

def view_summary(expenses):
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    
    totals = {}
    
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in totals:
            totals[category] = 0

        totals[category] += amount

    print("\n--- Summary by Category ---")
    for category, total in totals.items():
        print(f"{category}: ${total:.2f}")
        
def delete_expense(expenses):
    view_expenses(expenses)
    index = int(input("Enter the number of the expense to delete: ")) - 1

    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        save_expenses(expenses)
        print(f"Deleted: ${removed['description']}")
    else:
        print("Invalid number.")

def main():
        expenses = load_expenses()

        while True:
            print("\n--- Expense Tracker ---")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. View Summary")
            print("4. Delete Expense")
            print("5. Quit")

            choice = input("Choose an option: ")

            if choice == "1":
                add_expense(expenses)
            elif choice == "2":
                view_expenses(expenses)
            elif choice == "3":
                view_summary(expenses)
            elif choice == "4":
                delete_expense(expenses)
            elif choice == "5":
                break
            else:
                print("Invalid option. Please try again.")
main()
