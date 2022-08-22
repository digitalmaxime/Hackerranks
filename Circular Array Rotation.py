import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k):
    b = [None]*len(a)
    res = []
    for i in range(0, len(a)):
        idx = (i + 1 + k)%len(a) 
        if (idx == 0):
            idx = len(a)
        b[idx-1] = a[i] 
    for bees in b :
        print(bees)    

#SOLUTION PYTHON
# def circularArrayRotation(a, k, queries):
#     b = [None]*len(a)
#     res = []
#     for i in range(0, len(a)):
#         idx = (i + 1 + k)%len(a) 
#         if (idx == 0):
#             idx = len(a)
#         b[idx-1] = a[i]  
#     for q in queries:
#         res.append(b[q])
#         print(res[-1])

#     return res

#SOLUTION JAVA
# static int[] circularArrayRotation(int[] a, int k, int[] queries) {
        
#         int[] b = new int [a.length];
#         int[] res = new int[queries.length];
#         for(int i=0; i<a.length; i++) {
#             int idx = (i + 1 + k)%(a.length);
#             if (idx == 0) {
#                 idx = a.length;
#             }
#             b[idx-1] = a[i];
#         }
#         for(int i=0; i<queries.length; i++){
#             res[i] = b[queries[i]];
#         }
#         return res;

if __name__ == '__main__':
    a = [1, 3, 5, 7]
    k = 2
    circularArrayRotation(a, k)
else :
    print("what;s going on with the main() ?? ")