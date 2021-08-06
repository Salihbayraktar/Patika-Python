def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)

l1 = [10, 5,4,3,2,1,5, 2, 3, 7, 5]
s = 10
print(sum_pairs(l1,s))




"""
def sum_pairs(ints, s):
    minusList = []
    intsDict = {}
    for i in range(len(ints)):
        if ints[i] not in intsDict:
            intsDict[ints[i]] = i
        else:
            pass
        # print( intsDict[ints[i]])
        minusList.append(s - ints[i])

    print("ekleme işi bitti")
    print(intsDict)
    print(minusList)
    result = []
    for i in range(len(minusList)):
        try:
            # print(ints[i+1:])
            second = ints[i + 1:].index(minusList[i]) + i + 1
            result.append(str(i) + str(second))
        except:
            pass
    print(result)
"""
