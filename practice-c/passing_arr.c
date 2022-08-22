#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int* multiplyArrayBy1000(int* ptr, int size) {
    int i;

    for (i = 0; i<size; ++i) {
        ptr[i] = 1000*ptr[i];
    }
    return ptr;
}

void print(int * ptr, int size) {
    int i;
    for (i = 0; i<size; ++i) {
            printf("value of arr[%d] : %d \n", i, ptr[i]);
        }
}

int main() {

    int arr1[5] = {0, 1, 2, 3, 4};
    int arr2[5] = {10, 11, 12, 13, 14};
    int arr3[5] = {0};

    multiplyArrayBy1000(arr2, 5);

    print(arr1, 5);
    print(arr2, 5);
    print(arr3, 5);


    return 0;
}