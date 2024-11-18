#include <stdio.h>
float income,rent, utilities, groceries, transportation, savings, expenses, spend;

float input(char type[],float var){
printf("monthly %s: \n", type);
scanf("%f",&var);
return var;
}

void percent (char type[], int amount){
    int per = amount/income *100;
    printf ("Your %s  is %d%% of your income.\n", type, per);
}



int main (void){
    float prent, putilties,pgroceries, ptransportation, psavings, pexpenses;
    print("This is your budget calculator.\n");
    income = input ("income", income);
    rent = input ("rent",rent);
    utilities = input ("utilities",utilities);
    groceries = input ("groceries",groceries);
    transportation = input ("transportation", transportation);
    savings = income * .2;
    expenses = rent + utilities + groceries + transporation;
    spend = income - expenses - savings;
    printf ("You make $%.2f\n", income);
    printf ("Your expenses are $%.2f\n", expenses);
    printf ("Your savings are $%.2f\n",savings);
    printf("YOur spending money is $%.2f\n", spend);

    percent("rent",rent);
    percent("utilities", utilities);
    percent("groceries", groceries);
    percent("transportation",transportation);
    percent("expenses",expenses);
    percent("savings",savings);
    percent("spending money",spending);

    return 0;
}