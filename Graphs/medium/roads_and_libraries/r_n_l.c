#include <stdio.h>




long roadsAndLibraries(int n, int c_lib, int c_road, int cities_rows, int cities_columns, int** cities) {
// if (c_lib < c_road) :               # simple check if roads are just too expensive..
//         return (c_lib * n)
    
//     if (n == 1 or cities == None) :
//         return n * c_lib

    if (c_lib < c_road) {
        return (c_lib * n);
    }  

    if (n == 1) {
        return (n * c_lib);
    }

    return 0;

}


int main() {
    int** city_connections = {{2, 1}, {1, 3}, {4, 1}};
    int cost = roadsAndLibraries(6, 100, 1, 3, 4, city_connections);
    printf(cost);

    return 0;

}