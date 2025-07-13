MonthlyIncome = int(input("Enter your monthly income: "))
MonthlyExpenses = int(input("Enter your total monthly expenses: "))
MonthlySavings = MonthlyIncome - MonthlyExpenses
rate = 0.05
ProjectedSavings = MonthlySavings * (1 + rate) ** 12
print("Projected savings after one year, with interest, is:", ProjectedSavings)