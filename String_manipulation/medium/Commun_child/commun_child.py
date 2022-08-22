def commonChild(s1, s2):
    temp1 = s1
    temp2 = s2
    for i in range(len(s2)):
        if s2[i] not in temp1:
            temp2 = temp2.replace(s2[i], '')
    
    s2 = temp2
   
    for i in range(len(s1)):
        if s1[i] not in s2:
            temp1 = temp1.replace(s1[i], '')
    
    s1 = temp1
    
    print(s1)
    print(s2)
    
    maxLength = 0
    for i in range(len(s1) - 1, -1, -1):
        currentLength = 0
        s1Iterator = i
        s2Iterator = len(s2) - 1
        
        while s1Iterator >= 0:
            while s2Iterator >= 0:
                if s2[s2Iterator] == s1[s1Iterator]:
                    currentLength += 1
                    s2Iterator -= 1 
                    break
                s2Iterator -= 1
            s1Iterator -= 1
        if currentLength > maxLength:
            maxLength = currentLength
            
    return maxLength

s1 = 'WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS'
s2 = 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'
# s1 = 'SHINCHAN'
# s2 = 'NOHARAAA'
ans = commonChild(s1, s2)
print(ans)