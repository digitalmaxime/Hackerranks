#include <stdio.h>
#include <time.h>
#include <stdlib.h> 

int * getRandom();


int main() {
    int* p = NULL;
    p = getRandom();

    printf("Value of p[0] : %d \n", p[0]);


    return 0;
}

int * getRandom() {
    int i;
    static int ptr[5];

    time_t t;
    /* Intializes random number generator */
    srand((unsigned) time(&t));

    for (i = 0; i<5; ++i) {
        ptr[i] = rand();
        printf("value of ptr{%d} : %d\n", i, *ptr);
        
    }
    

    return ptr;
}