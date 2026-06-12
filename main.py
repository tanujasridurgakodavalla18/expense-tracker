expenses = []

while True:
    print("\n💰 EXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append((item, amount))
        print("Expense added!")

    elif choice == "2":
        print("\n--- Expenses ---")
        for item, amount in expenses:
            print(item, ":", amount)

    elif choice == "3":
        total = sum(amount for item, amount in expenses)
        print("Total Expense:", total)

    elif choice == "4":
        print("Exit")
        break
