#include <stdio.h>

int main(void){
    char name[9];
    printf("what is your name?\n");
    scanf("%s", name);
    printf("Hello %s\n", name);
    return 0;
}