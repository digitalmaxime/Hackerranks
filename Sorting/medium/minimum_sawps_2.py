def minimumSwaps(arr):
    nbOfSwaps = 0
    dic = dict()
    
    for i in range(len(arr)):
        if arr[i] != i + 1:
            dic[i+1] = arr[i]
    
    for key, val in dic.items():
        if (key != val):
            # needsMoreWork = True
            while(dic[key] != key):
                temp = dic[key]
                dic[key] = dic[temp]
                dic[temp] = temp
                nbOfSwaps += 1
            
    return nbOfSwaps