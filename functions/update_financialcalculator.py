def user inputs(type):
    return float(input(f"monthly {type}"))

def divide (type, income):
    return type/ income *100 



income=float(input("what isn your monthly income: "))
rent= float(input("what is your monthlyrent: "))
utilities=float(input("what is your monthly utilities: "))
groceries= float(input("what is your monthly transportation: "))
saving = income *.2
expenses = rent + utilities + groceries + transporatation
spending = income -expenses -savings 

def percent(type,amount):
    per = amount/income *100

    return(f"your {type} is {per}% income. ")


print(f"Your monthly income is ${income}\n")
print(f"Your monthly expenses are ${expenses}\n")
print(f"Your monthly savings is ${savings}\n")
print(percent("rent", rent))
print(percent("utilities",utilities))
print(percent("groceries", groceries))
print(percent("transportation", transportation))
print(percent("savings",savings))
print(percent("expenses",expenses))