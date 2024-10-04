#include <stdio.h>

int main(void){
    float income, rent, utilities, groceries, transportation, savings, expenses, total;
    float prent, putilities, pgroceries, ptransportation, psavings, pexpenses;
    printf("Hello and welcome to our budget calculator\n");
    printf("How much do you make each month?");
    scanf("%f", &income);
    printf("How is your rent?");
    scanf("%f", &rent);
    printf("How are your utilities?");
    scanf("%f", &utilities);
    printf("How are your groceries?");
    scanf("%f", &groceries);
    printf("How is your transportation?");
    scanf("%f", &transportation);
    expenses = rent + utilities + groceries + transportation;
    savings = income * .2;
    total = income - savings - expenses 
    ;printf("Your monthly income is $%.2f\n", income);
    printf("Your monthly expenses is $%.2f\n", expenses);
    printf("Your monthly savings is $%.2f\n", savings);
    printf("You have $%.2f left to spend\n", total, "left that you can spend ")
    ;prent = rent/income *100;
    ;putilities = utilities/income *100;
    pgroceries = groceries/income *100;
    ptransportation = transportation/income *100;
    ;pexpenses = expenses/income *100;
    psavings = savings/income *100;
    printf("Your expenses are %.1f%% of your income\n", pexpenses);
    ;return 0;
}