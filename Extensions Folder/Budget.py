print("Budget calculator")
income = float (input ('what is your monthly income?'))
rent = float(input ('what is your monthly rent?'))
utilities = float(input ('what is your monthly utilities?'))
groceries = float(input ('what is your monthly groceries?'))
transportation = float(input ('what is your monthly transportation?'))
expenses = rent + utilities + groceries + transportation;
savings = income * 0.2
total = income - savings - expenses -savings
prent = rent/income *100 
putilities = utilities/income *100
ptransportation = transportation/income *100
pexpenses = expenses/income *100
print("Your income is: %\n", income)
print("Your expenses are: %\n", expenses)
print("Your saving are: %\n", savings)
print ("YOur total left to spend is: $%.2f\n", total)
print ( "Your rent is % of your income ", prent)
print("Your rent is % of your income", putilities)
print("Your rent is % of your income", ptransportation)
