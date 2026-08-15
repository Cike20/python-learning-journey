number_of_expenses = int(input("Enter the number of expenses you want to track: "))
expenses = []
total = 0
category_totals = {}
highest_category = ""
highest_category_total = 0
for number in range(1, number_of_expenses + 1):
    category = input(f"Enter category for expense {number}: ")
    amount = int(input(f"Enter amount for expense {number}: "))
    expense = {
        "category": category,
        "amount": amount,
    }
    expenses.append(expense)
    total += amount
    if category in category_totals:
        category_totals[category] += amount
    else:
        category_totals[category] = amount
print(f"Total expenses: {total} HUF")
for category, category_total in category_totals.items():
    if total > 0:
        percentage = (category_total / total) * 100
    else:
        percentage = 0
    print(f"Total for {category}: {category_total} HUF ({percentage:.2f}%)")
    if category_total > highest_category_total:
        highest_category_total = category_total
        highest_category = category
for i, expense in enumerate(expenses, start=1):
    print(f"Expense {i}: {expense['category']} - {expense['amount']} HUF")
if number_of_expenses > 0:
    print(f"Category with highest total: {highest_category} ({highest_category_total} HUF)")
else:
    print("No expenses were entered.")