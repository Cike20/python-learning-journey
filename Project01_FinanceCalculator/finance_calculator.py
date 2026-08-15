monthly_salary = int(input("What is your monthly salary?"))
monthly_expenses = int(input("What are your monthly expenses?"))
desired_monthly_savings = int(input("What is your desired monthly savings?"))
monthly_savings = monthly_salary - monthly_expenses
yearly_savings = monthly_savings * 12
difference = monthly_savings - desired_monthly_savings
if monthly_salary <= 0:
    savings_rate = "Cannot be calculated"
    print("Savings Rate: Cannot be calculated")
else:
    savings_rate = monthly_savings / monthly_salary * 100
    print("Savings Rate:", savings_rate, "%")
print("Monthly Savings:", monthly_savings)
if monthly_expenses > monthly_salary:
    print("Warning: You are spending more than you earn!")
print("Yearly Savings:", yearly_savings)
if monthly_savings > desired_monthly_savings:
    print("Congratulations! You are saving", difference, "more than your desired savings.")
elif monthly_savings < desired_monthly_savings:
    print("You are saving", abs(difference), "less than your desired savings.")
else:
    print("Congratulations! You are saving exactly your desired savings.")