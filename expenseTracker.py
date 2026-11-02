
expenses = []

def add_expense():
    name = input("Enter Expense Name: ")
    amount = float(input("Enter Amount: "))
    category = input("Enter Category: ")

    expense = {
        "Name": name,
        "Amount": amount,
        "Category": category
    }

    expenses.append(expense)
    print("Expense Added Successfully!")


def view_expenses():
    if not expenses:
        print("No Expenses Found!")
    else:
        print("\n--- Expense Details ---")

        for expense in expenses:
            print("Name:", expense["Name"])
            print("Amount: Rs.", expense["Amount"])
            print("Category:", expense["Category"])
            print("----------------------")


def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["Amount"]

    print("Total Expenses: Rs.", total)


def search_expense():
    category = input("Enter Category to Search: ")

    found = False

    for expense in expenses:
        if expense["Category"].lower() == category.lower():
            print(expense)
            found = True

    if not found:
        print("No Expenses Found in this Category!")


def delete_expense():
    name = input("Enter Expense Name to Delete: ")

    for expense in expenses:
        if expense["Name"].lower() == name.lower():
            expenses.remove(expense)
            print("Expense Deleted Successfully!")
            return

    print("Expense Not Found!")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Search Expense")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        search_expense()

    elif choice == "5":
        delete_expense()

    elif choice == "6":
        print("Thank You for Using Expense Tracker!")
        break

    else:
        print("Invalid Choice! Try Again.")
