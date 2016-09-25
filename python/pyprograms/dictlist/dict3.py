# dictionaries

def makeInverseIndex(strList):
    numStrList = list(enumerate(strList))
    n = 0
    dictionary = {}
    while (n < len(strList)):
        for word in numStrList[n][1].split():
            if word not in dictionary:
                dictionary[word] = {numStrList[n][0]}
            elif {numStrList[n][0]} not in dictionary[word]:
                dictionary[word]|={numStrList[n][0]}
        n = n+1

    return dictionary

L=['A B C', 'B C E', 'A E', 'C D A']
#    0        1        2      3

print makeInverseIndex(L)