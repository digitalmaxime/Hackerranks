def sherlockAndAnagrams(s):
    # Write your code here
    result = 0
    
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            dic1 = {}
            dic2 = {}
            for k in range(j-i):
                if s[i+k] in dic1:
                    dic1[s[i+k]] += 1
                else:
                    dic1[s[i+k]] = 1
                    
                if s[j-k] in dic2:
                    dic2[s[j-k]] += 1
                else:
                    dic2[s[j-k]] = 1
                    
                if dic1 == dic2:
                    result += 1
                        
    return result