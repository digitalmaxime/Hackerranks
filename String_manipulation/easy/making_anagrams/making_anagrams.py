def makeAnagram(a, b):
    # Write your code here
    a = sorted(a)
    b = sorted(b)
    # minLength = min(len(a), len(b))
    nbOfDeletion = 0
    counterA = 0
    counterB = 0
    while counterA < len(a) and counterB < len(b):
        if a[counterA] != b[counterB]:
            nbOfDeletion += 1
            if a[counterA] > b[counterB]:
                counterB += 1
            else:
                counterA +=1
        else:
             counterA += 1   
             counterB += 1   
    
    nbOfDeletion += len(a) - counterA
    nbOfDeletion += len(b) - counterB
    return nbOfDeletion