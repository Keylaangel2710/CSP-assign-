#include <stdio.h>


float first, after, verb, noun, sentence;


int main(void){
    char name[20], first [20],place [20], after [20], verb [20], noun [20], sentence [320];
    print("Type a name: ");
    scanf("%s", &name);
    printf("Type a place: ");
    scanf("%s", &place);
    printf("type a verb: ");
    scanf("%s", &verb);
    printf("Type a noun: ");
    scanf("%s", &noun);
    strcat(sentence, name);
    strcat(sentence, "went to the kitchen");
    strcat(sentence, place);
    strcat(sentence, "started dancing");
    strcat(sentence, verb);
    strcat(sentence, " with a toast in his hand");
    strcat(sentence, noun);
    printf("%s", sentence);
    return 0;
}
    






}