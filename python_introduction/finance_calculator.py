income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
Monthly_Savings = income - expenses
print("Your monthly savings are $", Monthly_Savings)
Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)
print("Projected savings after one year, with interest, is:" , Savings)