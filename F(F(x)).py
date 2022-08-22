
#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    
    dict1 = {}
    dict2 = {}
    for i in range(0, len(p)) :
        dict1[i+1] = p[i]
    for i in range(0, len(p)) :
        dict2[p[i]] = i+1

    arr_key = list(dict1.keys())
    arr_val = list(dict1.values())
    #print(arr_key)
    #print(arr_val)
    
    result = []
    for i in range(1, len(arr_val)+1) : 
        key1 = dict2[i]
        key2 = dict2[key1]
        result.append(key2)
    print(result)
    
if __name__ == '__main__':
    p = [4,3,5,1,2]
    permutationEquation(p)