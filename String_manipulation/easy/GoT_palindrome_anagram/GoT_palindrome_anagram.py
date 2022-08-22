# Complete the gameOfThrones function below.
def gameOfThrones(s):
    print("In game of thrones!")
    if len(s) % 2 == 0:
        even = True
    else:
        even = False

    arr = []
    number_of_unpaired = 0 #should not exced 1
    paired = True
    print("len of s : " + str(len(s)))
    for i in range(len(s)):
        if s[i] not in arr:
            arr.append(s[i])
            # print(s[i])
            # count = 0
            # for element in s:
            #    if element == s[i]:
            #         count += 1
            # print(count)
            count = s.count(s[i])
            if not (count % 2 == 0):
                paired = False
                number_of_unpaired += 1
                if number_of_unpaired > 1:
                    return "NO it ain't"
    print("number of unpaired : " + str(number_of_unpaired))
    if paired == False and even is True:
        return "NO"
    else: 
        return "YES"

s1 = "aaabbbb"
s2 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzz"

answer = gameOfThrones(s1)
print("Can this string be rearanged to be a palindrome?")
print(answer)