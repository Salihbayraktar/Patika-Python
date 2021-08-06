def letterCounter(s):
    letterCounterDict = {}
    for i in s:
        if i.islower():
            if i not in letterCounterDict:
                letterCounterDict[i] = 1
            else:
                letterCounterDict[i] += 1
    return letterCounterDict


def mix(s1, s2):
    s1Letters = letterCounter(s1)
    s2Letters = letterCounter(s2)
    resultDict = {}
    for k in s1Letters.keys():
        if k in s2Letters:
            if s1Letters[k] > s2Letters[k] and s1Letters[k] > 1:
                letterStr = k * s1Letters[k]
                resultDict[letterStr] = '1'
            elif s2Letters[k] > s1Letters[k] and s2Letters[k] > 1:
                letterStr = k * s2Letters[k]
                resultDict[letterStr] = '2'
            elif s1Letters[k] == s2Letters[k] and s1Letters[k] > 1:
                letterStr = k * s1Letters[k]
                resultDict[letterStr] = '='
            del s2Letters[k]
        else:
            if s1Letters[k] > 1:
                letterStr = k * s1Letters[k]
                resultDict[letterStr] = '1'
    for k in s2Letters.keys():
        if s2Letters[k] > 1:
            letterStr = k * s2Letters[k]
            resultDict[letterStr] = '2'
    resultList = sorted(resultDict.items(), key=lambda x: (-len(x[0]), x[1], x[0]))
    result = ''
    for i in range(len(resultList)):
        num = str(resultList[i][1])
        if i != len(resultList) - 1:
            result += num + ':' + resultList[i][0] + '/'
        else:
            result += num + ':' + resultList[i][0]
    return result


print(mix("Are they here", "yes, they are here"))
print(mix("looping is fun but dangerous", "less dangerous than coding"))
