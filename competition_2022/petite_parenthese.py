def check(str) :
    symbols = []
    closingSymbols = {")", "}", "]"}
    validSymbols = {"(", "{", "[", ")", "}", "]"}
    closeOpenDic = {")":"(", "}":"{", "]":"["}
    
    for char in str:
        if char in validSymbols:
            symbols.append(char)
            
    idxClosing = 0
    while idxClosing < len(symbols):
        if symbols[idxClosing] in closingSymbols:
            matchingOpeningSymbol = closeOpenDic[symbols[idxClosing]]
            if idxClosing == 0 or symbols[idxClosing - 1] != matchingOpeningSymbol:
                print("False")
                return
            symbols.pop(idxClosing)
            symbols.pop(idxClosing - 1)
            idxClosing -= 1
        else :
            idxClosing += 1
    
    if len(symbols) > 0:
        print("False")
        return
    
    print("True")
    
# str = "((([])))(()){}[{}]"
# str = "[](){}[{()}]((()))"
# str = "() {} [] [{()}] {{}{{}}} (([[]]{{}})(([{}{}[]])))" # TRUE
# str = "{{}{{}}}" # TRUE
# str = "{{}{{}}" # False
# str = "{{}}}{" # False
# str = "{ {}} } {} []]" # False
# str = "{ {{}}{} }" # True
# str = "( {} [{()}] [] )" # True
# str = "(){(){()}}" # True
# str = "(([){)}]" # False
# str = "[[[[{{{{[[[[(((())))]]]]}}}}]]]]" # TRUE
# str = "[{()]}" # False
# str = "{()}{[]}" # True
# str = "{()}{[}]" # False
# str = "{()}{[}]" # False
# str = "{()}{[](})" # False
str = "((()){[]{[]}})" # True

check(str)