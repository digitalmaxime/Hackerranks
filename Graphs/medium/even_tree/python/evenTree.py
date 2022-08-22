import math
import os
import random
import re
import sys


# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to):
    graph = {}
    for i in t_to:
        graph[i] = []
    print(graph)
    count = 0
    for i in t_to:
        graph[i].append(t_from[count])
        count += 1
    print(graph)

    def inner_recursion(key, counter):
        for node in graph[key]:
            # print(node)
            counter += 1
            if node in graph:
                inner_recursion(node, counter)
        return counter

    number_of_cuts = 0
    for i in range(1, t_nodes):
        if i in graph:
            parent = graph[i]
            print("Parent : " + str(i))
            for child in parent:
                print('\tchild : ' + str(child) )
                counter = 0
                if child in graph:
                    number_of_child = inner_recursion(child, counter)
                    print ("\tcount number of his own immediate child: " + str(number_of_child))
                    if (number_of_child %2 != 0):
                        number_of_cuts += 1
    print("number of cuts : " + str(number_of_cuts))
    return number_of_cuts


t_from = [2, 3, 4, 5, 6, 7, 8, 9, 10]
t_to = [1, 1, 3, 2, 1, 2, 6, 8, 8 ]
evenForest(10, 9, t_from, t_to)


#graph = {t_from[i]: t_to[i] for i in range(len(t_from))}
#graph = dict(zip(t_from, t_to))
#inv_map = {v: k for k, v in graph.items()}
# print(inv_map)
