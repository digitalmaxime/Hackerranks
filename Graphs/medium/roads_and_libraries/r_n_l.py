import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def roadsAndLibraries(n, c_lib, c_road, cities):
    if (c_lib < c_road) :               # simple check if roads are just too expensive..
        return (c_lib * n)
    
    if (n == 1 or cities == None) :
        return n * c_lib
    
    visited_cities = set()
    cycles_set = dict()

    for i in range(len(cities)) :
        cycles_set[i] =   set(cities[i])
        visited_cities.add(cities[i][0])
        visited_cities.add(cities[i][1])
    
    print(cycles_set)

    #join cycle with common nodes ---> O(n^2) .. not good
    for i in range (len(cycles_set)) :
        for j in range(len(cycles_set)) :
            if i != j and cycles_set[i] & cycles_set[j] :
                cycles_set[i] = cycles_set[i] | cycles_set[j]
                cycles_set[j].clear()
    
    #calculate number of libraries and roads
    number_of_libraries = 0
    number_of_roads = 0;
    for cycle in cycles_set.values() :
        if len(cycle) != 0 :
            number_of_libraries += 1
            number_of_roads += (len(cycle) - 1)
    # calculate cost
    total_cost = (number_of_libraries * c_lib + number_of_roads * c_road)
    if n > len(visited_cities) :
        total_cost += (n - len(visited_cities)) * c_lib

    print(cycles_set)
    return total_cost


if __name__ == '__main__':

    city_connections = [[6,4], [3,2], [7, 1], [4,7]]
    cost = roadsAndLibraries(2, 102, 1, city_connections)
    print(cost)