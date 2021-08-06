def find_and_sum_prime_numbers(n, resultDict):
    rawN = n
    n = abs(n)
    i = 2
    primeSet = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in resultDict:
                resultDict[i] = rawN
            elif i not in primeSet:
                resultDict[i] += rawN
            primeSet.add(i)
    if n > 1:
        if n not in resultDict:
            resultDict[n] = rawN
            primeSet.add(n)
        elif n not in primeSet:
            resultDict[n] += rawN
    return resultDict


def sum_for_list(lst):
    resultDict = {}
    for i in lst:
        resultDict = find_and_sum_prime_numbers(i, resultDict)

    resultList = sorted(resultDict.items(), key=lambda x: x[0])   # Engin hocaya sonucu tuple değil de list olarak elde edip edemeyeceğimizi sor
    print(resultList)

    resultList2 = sorted([k,v] for k,v in resultDict.items())

    print(resultList2)


    for i in range(len(resultList)):
        resultList[i] = list(resultList[i])                       #
    print(resultList)

    return resultList


list2 = [902357, -968097, -627144, -652087, -429945, 11194, -494131, -506621, -738142, -630425, 808045, -70747, -50136, -441806, -334532]
#list2 = [12, 15]
sum_for_list(list2)

"""
    primeNumbers = set()

    for i in range(3, maxNumber + 1, 2):
        isPrime = True
        for j in range(3, i, 2):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primeNumbers.add(i)
        print(i)
    return primeNumbers
    """

"""
def sum_for_list(lst):
    primeNumbers = find_prime_numbers(964644)
    print(primeNumbers)
    # primeNumbers = find_prime_numbers(abs(lst[len(lst)-1]))
    # primeNumbers = find_prime_numbers(409007)
    # print(primeNumbers)
    primeDict = {}


sum_for_list([9984194949455489949])
"""
