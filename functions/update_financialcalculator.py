def user_inputs(type):
    return float(input(f"monthly {type}"))

def divide (type, income):
    return type/ income *100 



income= user_inputs("income:")
rent= user_inputs("rent:")
utilities= user_inputs("utilities:")
groceries= user_inputs("groceries:")
transportation = user_inputs("transportation:")
saving = income *0.2
expenses = rent + utilities + groceries + transportation
spending = income-int (expenses) -saving

def percent(type,amount):
    per = amount/income *100

    return(f"your {type} is {per}% income. ")

print(percent("rent", rent))
print(percent("utilities",utilities))
print(percent("groceries", groceries))
print(percent("transportation", transportation))
print(percent("savings",savings))
print(percent("expenses",expenses))