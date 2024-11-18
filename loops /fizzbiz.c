#include <stdio.h>
#include <string.h>
int i;
int user;
char one [50];
char two [50];
char three [50];
int main (){
    printf ("please give me a number\n");
    scanf("%d", &user);
    printf ("Give me a short word\n");
    scanf("%s",one);
    printf("give me another short word\n");
    scanf("%s",two);
    strcat(three, one);
    strcat("three, two");
    //loops thats counts to 20
    for (i=1;i<=user;i++){
    //replace #'s divisible by 3 and 5 with "fizzbuzz"
    if(i%3==0 && 1%5==0){
       printf("%s\n",three);
    } else if (i%3==0){
        //replace #'s divisible by 3 with "fizz"
        printf("%s\n", one);
    }else if (i%5==0){
        //replace #'s divisible bt 5 with "Buzz"
        printf("%s\n", two);
    }else {
        printf("%d\n", i);//print the number 
    }

    }
    return 0;