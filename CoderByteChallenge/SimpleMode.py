def NumberCounter(arr):
    resultDict = {}
    for i in arr:
        if i not in resultDict:
            resultDict[i] = 1
        else:
            resultDict[i] += 1
    return resultDict


def SimpleMode(arr):
    numberDict = NumberCounter(arr)
    numberDict = dict(sorted(numberDict.items(), key=lambda item: -item[1]))
    result = -1
    minIndex = len(arr)
    maxRepeat = numberDict[next(iter(numberDict))]
    if maxRepeat == 1:
        return -1
    for k, v in numberDict.items():
        if v == maxRepeat:
            currentIndex = arr.index(k)
            if currentIndex < minIndex:
                minIndex = currentIndex
                result = k
        else:
            break
    return result


print(SimpleMode([7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 9, 8, 7]))
