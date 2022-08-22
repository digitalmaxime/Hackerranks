def whatFlavors(cost, money):
    # Write your code here
    currentSpending = 0
    solution = []
    originalCost = cost
    cost = sorted(cost)
    
    
    mapValueToIndex = dict()
    for i in range(len(originalCost)):
        print('mapValueToIndex.keys()', mapValueToIndex.keys())
        if originalCost[i] in mapValueToIndex.keys():
            mapValueToIndex[originalCost[i]].append(i)
        else:
            mapValueToIndex[originalCost[i]] = [i]
    
    # mapValueToIndex = {v:k for k, v in enumerate(originalCost)}

    it1 = 0
    it2 = len(cost) - 1
        
    while it1 < it2:
        tempSum = cost[it1] + cost[it2]
        if tempSum == money:
            index1 = mapValueToIndex[cost[it1]][0]
            index2 = mapValueToIndex[cost[it2]][0]
            if index1 == index2:
                index2 = mapValueToIndex[cost[it2]][1]
            solution = [min(index1, index2) + 1, max(index1, index2) + 1]
            print(solution[0], solution[1])
            return
            
        if tempSum > money:
            it2 -= 1
                
        elif tempSum < money:
            if tempSum > currentSpending:
                currentSpending = tempSum
                
                index1 = mapValueToIndex[cost[it1]][0]
                index2 = mapValueToIndex[cost[it2]][0]
                if index1 == index2:
                    index2 = mapValueToIndex[cost[it2]][1]
                solution = [min(index1, index2) + 1, max(index1, index2) + 1]
            it1 += 1
            
    print(solution[0], solution[1])

    
cost = [1, 4, 5, 3, 2, 3]
ans = whatFlavors(cost , 4)

