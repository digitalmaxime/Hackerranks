def getMinimumCost(k, c):
    c.sort(reverse=True)
    
    dic = dict()
    for i in range(k):
        dic[i] = 1
    
    price = 0
    for i in range(len(c)):
        personIndex = i % k
        print(personIndex)
        print(personIndex)
        price += dic[personIndex] * c[i]
        dic[personIndex] +=1
    
    return price
