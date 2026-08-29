from pathlib import Path
import csv
from datetime import datetime

folder = Path("exports")

all_transactions = []
invalid_rows = 0
total_amount = 0
category_totals = {}
largest_amount = 0
largest_description = ""
largest_date = ""
largest_category = ""

for file in folder.iterdir():
    if file.suffix.lower() == ".csv":
        print(file.name)

        with open(file, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=";")

            next(reader)
            
            for row in reader:
                if len(row) != 4:
                    print(f"Skipped invalid row: {row}")
                    invalid_rows += 1
                    continue
                try:
                    datetime.strptime(row[0], "%Y.%m.%d")
                except ValueError:
                    print(f"Skipped invalid date: {row}")
                    invalid_rows += 1
                    continue
                try:
                    amount = int(row[3])
                except ValueError:
                    print(f"Skipped invalid amount: {row}")
                    invalid_rows += 1
                    continue
                
                all_transactions.append(row)
                category = row[2]
                if amount > largest_amount:
                    largest_amount = amount
                    largest_date = row[0]
                    largest_description = row[1]
                    largest_category = category
                total_amount += amount
                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount

number_of_transactions = len(all_transactions)

if number_of_transactions > 0:
    average_transaction = total_amount / number_of_transactions
else:
    average_transaction = 0

all_transactions.sort(key=lambda transaction: transaction[0])

with open("consolidated_transactions.csv", "w", newline="") as output_file:
    writer = csv.writer(output_file, delimiter=";")

    writer.writerow(["Date", "Description", "Category", "Amount"])

    for transaction in all_transactions:
        writer.writerow(transaction)

for transaction in all_transactions:
    print(transaction)

print(f"Total amount: {total_amount} HUF")

for category, amount in category_totals.items():
    print(f"{category}: {amount} HUF")

print(f"Number of transactions: {number_of_transactions}")
print(f"Average transaction: {average_transaction:.0f} HUF")

if number_of_transactions > 0:
    print(
        f"Largest transaction: {largest_date} - "
        f"{largest_description} - {largest_category} - "
        f"{largest_amount} HUF"
    )
print(f"Invalid rows skipped: {invalid_rows}")