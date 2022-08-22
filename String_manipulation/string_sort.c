#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lexicographic_sort(const char* a, const char* b) {
    while (*a != '\0' && *b != '\0') {
        if (*a < *b) {
            return -1;
        }
        else if (*a > *b) {
            return 1;
        }
        a++;
        b++;
    }
    return 0;
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    while (*a != '\0' && *b != '\0') {
        if (*a > *b) {
            return -1;
        }
        else if (*a < *b) {
            return 1;
        }
        a++;
        b++;
    }
    return 0;}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    const char* copyA = a;
    const char* copyB = b;
    
    char alphabetA[26] = {0};
    int scoreA = 0;
    while (*a != '\0') {
        if (alphabetA[(*a) - 'a'] == 0) {
            alphabetA[(*a) - 'a'] = 1;
            scoreA++;
        }
        a++;
    }
    char alphabetB[26] = {0};
    int scoreB = 0;
    while (*b != '\0') {
        if (alphabetB[(*b) - 'a'] == 0) {
            alphabetB[(*b) - 'a'] = 1;
            scoreB++;
        }
        b++;
    }
    if (scoreA > scoreB) {return 1;}
    else if (scoreB > scoreA) {return -1;}
    else {
        return lexicographic_sort(copyA, copyB);
    }
        
}

int sort_by_length(const char* a, const char* b) {
    const char* copyA = a;
    const char* copyB = b;

    int lengthA = 0;
    while (*a != '\0') {
        lengthA++;
        a++;
    }
    int lengthB = 0;
    while (*b != '\0') {
        lengthB++;
        b++;
    }
    if (lengthA > lengthB) {
        return 1;
    }
    if (lengthA < lengthB) {
        return -1;
    }
    return lexicographic_sort(copyA, copyB);
}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a, const char* b)){
    int j;
    char* temp;
    for (int i=1; i<len; i++) { //insert sort algo
        temp = arr[i];
        for (j=i; j>0 && cmp_func(temp, arr[j-1]) < 0; j--) { 
            arr[j] = arr[j-1];
        }
        arr[j] = temp;
    }
}


int main() 
{
    int n;
    printf("Enter number of strings n : ");
    scanf("%d", &n);
  
    char** arr = (char**)malloc(n * sizeof(char*));
  
    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(4 * sizeof(char));
        printf("Enter string %d : ", i);
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }

    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("-----\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    //free memory
    for(int i = 0; i < n; i++){
        free(arr[i]);       
    }
    free(arr);
}