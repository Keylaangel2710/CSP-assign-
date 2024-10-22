print("Budget calculator")
print("Hello and welcome to our budget calculator\n");

income = input ('what is your monthly income?');
rent = input ('what is your monthly rent?');
utilities = input ('what is your monthly utilities?');
groceries = input ('what is your monthly groceries?');
transportation = input ('what is your monthly transportation?');
expenses = rent + utilities + groceries + transportation;
savings = income * .2;
total = income - savings - expenses 


print ("Your monthly income is ${income:.2f}\n")
print("Your monthly expenses are ${expenses:.2f}\n")
print("Your monthly savings is ${savings:.2f}\n")
print("Your monthly spending money ${spending:. 2f}\n")
print("Your rent is {int (prent)}% of your monthly income \n")
print("Your utilities are {int(putilities)}% of your monthly income \n")
print("Your groceries are {int(pgroceries)}% of your monthly income \n")
print("Your transportation is {int(ptransportation)}% of your monthly income \n")
print("Your savings are {int(psaving)}% of your monthly income \n")
print("Your expenses are {int(pexpenses)}% of your monthly income \n")