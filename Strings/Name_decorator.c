#include <stdio.h>

int main(void){
char name [20], sentence [20];
printf("Please type a name: ");
scanf("%s",  &name);
strcat(sentence, name)
printf("<<< %s >>>", name);
return 0;
}