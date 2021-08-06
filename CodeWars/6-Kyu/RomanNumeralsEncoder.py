def solution(n):
    symbolDict = {}
    symbolDict['M'] = n // 1000
    n = n % 1000
    symbolDict['CM'] = n // 900
    n = n % 900
    symbolDict['D'] = n // 500
    n = n % 500
    symbolDict['CD'] = n // 400
    n = n % 400
    symbolDict['C'] = n // 100
    n = n % 100
    symbolDict['XC'] = n // 90
    n = n % 90
    symbolDict['L'] = n // 50
    n = n % 50
    symbolDict['XL'] = n // 40
    n = n % 40
    symbolDict['X'] = n // 10
    n = n % 10
    symbolDict['IX'] = n // 9
    n = n % 9
    symbolDict['V'] = n // 5
    n = n % 5
    symbolDict['IV'] = n // 4
    n = n % 4
    symbolDict['I'] = n

    print(symbolDict)

    resultList = []
    for v, k in symbolDict.items():
        for i in range(k):
            resultList.append(v)
    return ''.join(map(str, resultList))


print(solution(1989))
