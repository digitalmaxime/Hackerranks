def luckBalance(k, contests):
    # Write your code here
    important = [x for x in contests if x[1] == 1]
    notImportant = [x for x in contests if x[1] == 0]
    
    def takeSecond(elem):
        return elem[0]

    important.sort(key=takeSecond, reverse=True) 
    
    answer = 0
    for i in range(min(k, len(important))):
        answer += important[i][0]
        
    for i in range(min(k, len(important)), len(important)):
        answer -= important[i][0]
        
    for ele in notImportant:
        answer += ele[0]
        
    return answer