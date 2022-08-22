s1 = "abc"
s2 = "abc cba"
s3 = "abc abd"
s4 = "abbcdabeef"
s5 = "xaxbbbxx"
s6 = "bbxxxaxb"


def anagrams(s):
    if len(s) % 2 != 0:
        return -1
    length_of_s = int(len(s)/2)
    word1 = list(s)[:length_of_s]
    word2 = list(s)[length_of_s:]
    dic1 = dict([(key, 0) for key in word1])
    dic2 = dict([(key, 0) for key in word2])
    res = 0
    dic1 = dict([(key, 0) for key in word1])
    dic2 = dict([(key, 0) for key in word2])
    for lettre in word1:
        dic1[lettre] += 1
    for lettre in word2:
        dic2[lettre] += 1
    for lettre in dic1:
        if lettre not in dic2:
            res += dic1[lettre]
        elif dic1[lettre] > dic2[lettre]: #attention au signe > (et non != )
            res += (dic1[lettre]-dic2[lettre]) #car ici on ne veut pas abs(num1-num2), just num1-num2
    return res
            
   
res4 = anagrams(s4)
print(res4)
res5 = anagrams(s5)
print(res5)
res6 = anagrams(s6)
print(res6)