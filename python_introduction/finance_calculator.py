monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
rate = 0.05
projected_savings = monthly_savings * (1 + rate) ** 12
print("Projected savings after one year, with interest, is:", projected_savings)
