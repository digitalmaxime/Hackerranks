def maxMin(k, arr):
    # Write your code here
    arr.sort()
    minUnfairness = float('inf')
    
    for i in range(len(arr) - k + 1):
        tempDifference = arr[i + k -1] - arr[i]
        if tempDifference < minUnfairness:
            minUnfairness = tempDifference
            
    return minUnfairness

arr = [100, 200, 300, 350, 400, 401, 402]
k = 3

print(maxMin(k, arr))