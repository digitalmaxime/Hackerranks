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
    
    g = dict()
    # create a bidirectional graph! (dic of sets)
    for i  in range(1, n+1) :
        g[i] = set()
    for i,j in cities:
        g[i].add(j) 
        g[j].add(i)
    print(g)

    seen = set()
    number_of_edges = 0
    number_of_cycles = 0

    # dfs returns number of connected cities (hence cities in a cycle)
    def dfs(key, number) :
        if key not in seen :
            seen.add(key)
            number += 1
            for val in g[key] :
                number = dfs(val, number)
        print("number : {}".format(number))
        return number

    # for each city (1 to n), find out number of connected cities
    for key in g.keys() :
        if key not in seen : # city is part of a new cycle
            number_of_cycles += 1
            number_of_edges += dfs(key, 0) - 1 # num connected cities -1 = num of roads (in a given cycle)

    print("number of edges : {}".format(number_of_edges))
    print("number of cycles : {}".format(number_of_cycles))

    return number_of_cycles * c_lib + (number_of_edges)* c_road



if __name__ == '__main__':

    city_connections = [[2, 1], [1,3], [4,1]]
    cost = roadsAndLibraries(6, 100, 1, city_connections)
    print(cost)
# 5 9 92 23
# 2 1
# 5 3
# 5 1
# 3 4
# 3 1
# 5 4
# 4 1
# 5 2
# 4 2