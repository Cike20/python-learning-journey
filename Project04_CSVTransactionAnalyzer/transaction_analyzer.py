import csv

total_amount = 0
category_totals = {}
largest_amount = 0
largest_description = ""
largest_category = ""
number_of_transactions = 0

with open("transactions.csv", "r") as file:
    reader = csv.reader(file, delimiter=";")
    next(reader)

    for row in reader:
        print(f"{row[1]} - {row[3]} HUF")

        amount = int(row[3])
        total_amount = total_amount + amount
        category = row[2]
        number_of_transactions += 1

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

        if amount > largest_amount:
            largest_amount = amount
            largest_description = row[1]
            largest_category = category

print(f"Total amount: {total_amount} HUF")

if number_of_transactions > 0:
    print(f"Average transaction amount: {total_amount / number_of_transactions:.0f} HUF")
    print(f"Largest transaction: {largest_description} - {largest_category} - {largest_amount} HUF")
else:
    print("No transactions to calculate average.")
    print("Largest transaction: No transactions found")

for category, category_total in category_totals.items():
    print(f"{category}: {category_total} HUF")

print(f"Number of transactions: {number_of_transactions}")

with open("transaction_summary.csv", "w", newline="") as summary_file:
    writer = csv.writer(summary_file, delimiter=";")

    writer.writerow(["Metric", "Value"])
    writer.writerow(["Total amount", total_amount])
    writer.writerow(["Number of transactions", number_of_transactions])

    if number_of_transactions > 0:
        writer.writerow(["Average transaction", f"{total_amount / number_of_transactions:.0f}"])
        writer.writerow([
            "Largest transaction",
            f"{largest_description} - {largest_category} - {largest_amount} HUF"
        ])
    else:
        writer.writerow(["Average transaction", "No transactions"])
        writer.writerow(["Largest transaction", "No transactions"])

    writer.writerow([])
    writer.writerow(["Category", "Total"])

    for category, category_total in category_totals.items():
        writer.writerow([category, category_total])