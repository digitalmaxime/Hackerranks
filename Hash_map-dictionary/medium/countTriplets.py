def countTriplets(arr, r):
    dic = dict()
    for ele in arr:
        if ele in dic:
            dic[ele] += 1
        else:
            dic[ele] = 1
    print(dic)
    
    result = 0
    for ele in dic:
        currentPosition = ele
        multRes = dic[currentPosition]
        
        # special case where r == 1
        if r == 1 and multRes < 3:
            continue
        elif r == 1 and multRes >= 3:
            print('dic[{}] =>'.format(currentPosition * r), dic[currentPosition * r])
            multRes = multRes * (multRes-1) * (multRes-2) / 6
            result += multRes
            print('special case : ', multRes)
            continue
        
        # normal case
        isSuccess = True
        for i in range(2):
            if (currentPosition * r in dic):
                print('dic[{}] =>'.format(currentPosition * r), dic[currentPosition * r])
                multRes *= dic[currentPosition * r]
                currentPosition *= r
                
            else:
                isSuccess = False                
                
        if isSuccess:
            result += multRes
    
    return result


arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
answer = countTriplets(arr, 1)