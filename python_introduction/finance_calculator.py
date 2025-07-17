month_income =int(input("Enter your monthly income: "))
month_expenses = int(input("Enter your total monthly expenses: "))

month_saving = month_income - month_expenses

projected_saving = month_saving * 12 + (month_saving * 12 * 0.05)

print(f"Your monthly savings are ${month_saving}")
print(f"Projected savings after one year, with interest, is: ${projected_saving}")