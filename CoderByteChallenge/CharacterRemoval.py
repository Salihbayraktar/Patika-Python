def LetterCounter(mainStr):
    resultDict = {}
    for i in mainStr:
        if i not in resultDict:
            resultDict[i] = 1
        else:
            resultDict[i] += 1
    return resultDict


def CharacterRemoval(strArr):
    mainStr = strArr[0]
    wordsList = strArr[1].split(',')
    wordsDict = dict(zip(wordsList, [0] * len(wordsList)))
    wordsDict = dict(sorted(wordsDict.items(), key=lambda item: -len(item[0])))
    for k in wordsDict.keys():
        mainStrDict = LetterCounter(mainStr)
        equalLetterCounter = 0
        for i in range(len(k)):
            if k[i] in mainStrDict:
                mainStrDict[k[i]] -= 1
                if mainStrDict[k[i]] < 0:
                    break
                equalLetterCounter += 1
            else:
                break
        if len(k) == equalLetterCounter:
            return len(mainStr) - len(k)
    return -1


# keep this function call here
print(CharacterRemoval(["wrdlmaeo", "a,b,c,d,ap,apple,bar,bat,cat,hello,y,yellow,w,wo,world,worr"]))


"""
9
TEST CASE POINTS
View incorrect test cases
1. For input ["wrdlmaeo", "a,b,c,d,ap,apple,bar,bat,cat,hello,y,yellow,w,wo,world,worr"] the output was incorrect. The correct output is 6
"""
