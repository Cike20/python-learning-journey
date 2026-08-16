def calculate_tax(income, tax_rate):
    tax = income * tax_rate
    return tax
def calculate_net_income(income, tax):
    net_income_after_tax = income - tax
    return net_income_after_tax
def is_valid_income(income):
    if income >= 0:
        return True
    else:
            return False
def is_valid_tax_rate(tax_rate):
    if tax_rate >= 0 and tax_rate <= 1:
        return True
    else:
        return False
number_of_calculations = int(input("How many calculations would you like to perform? "))
for number in range(1, number_of_calculations + 1):
    print(f"Calculation {number}")
    income = int(input("Enter your income: "))
    while not is_valid_income(income):
        print("Invalid income. Please enter a non-negative value.")
        income = int(input("Enter your income: "))
    tax_rate = int(input("Enter your tax rate: ")) / 100
    while not is_valid_tax_rate(tax_rate):
        print("Invalid tax rate. Please enter a value between 0 and 100.")
        tax_rate = int(input("Enter your tax rate: ")) / 100
    tax = calculate_tax(income, tax_rate)
    net_income = calculate_net_income(income, tax)
    print(f"Tax: {tax:.0f} HUF")
    print(f"Net Income: {net_income:.0f} HUF")
    print()