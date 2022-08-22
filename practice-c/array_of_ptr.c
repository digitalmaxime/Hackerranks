#include <stdio.h>

int main() {

    char *a = "maxime"; // equiv to char a[] = "maxime";
    printf("value of a : %s \n", a);

    char *c[] = {
        "mary",
        "puty",
        "rose"
    };

    for (int i = 0; i < 3; ++i) {
        printf("value of c[%d] : %s \n", i, c[i]);
    }

    return 0;
}