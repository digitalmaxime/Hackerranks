#include <stdio.h>
#include <stdint.h>

int main() {

    int arr[] = {1, 2, 3, 4, 5, 6};
    printf("address of &arr : %u \n", &arr); //&arr == arr ==&arr[0](its just an address)
    printf("address of &arr[0] : %u \n", &arr[0]); 
    printf("Value of arr : %u \n", arr);
    printf("Dereferenced arr : %u \n", *arr);
    printf("sizeOf arr : %ld \n", sizeof(arr));


    printf("---------------------\n");

    //int* ptr = arr; // equ to int* ptr = &arr[0]
    int* ptr = &arr[0];

    printf("address of ptr : %u \n", &ptr);
    printf("Value of ptr : %x \n", ptr);
    printf("Dereferenced ptr : %d \n", *ptr);
    printf("indexing ptr[0] : %d \n", ptr[0]);
    printf("sizeOf ptr : %ld \n", sizeof(ptr));

    printf("---------------------\n");

    int a[] = {1, 2, 3, 4, 5, 6};  
    ptr = (int*)(&a+1);  
    printf("%d \n", *(ptr-1) );

    // &array is an alias for &array[0] and returns the address of the first element in array
    // &pointer returns the address of pointer
//Difference ptr vs arr :
    // The less technical explanation: a is an address, p is an address which holds the address of a
    // explanation: to retrieve value from a[n], the computer starts at address a, moves n past it and 
    // fetches value from there; to retrieve value from p[n], the computer starts at address p, 
    // fetches the address stored there and adds n to it, then fetches value from the resulting address

    return 0;
}