#Expense Tracker
total_calculations=0
while True:

    expense = input("Enter expense amount (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    total_calculations +=float(expense)
    print("\nTotal Spent:",total_calculations)