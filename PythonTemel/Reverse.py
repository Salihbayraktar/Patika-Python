def reverseList(inputList):
    if type(inputList) == type(5):
        return

    for i in range(len(inputList)):
        if type(inputList[i]) == type(5):
            continue

        inputList[i] = inputList[i][::-1]
        reverseList(inputList[i])

    return inputList


inputList = [[1, 2], [3, 4], [5, 6, 7]]
print(reverseList(inputList[::-1]))

inputList2 = [[1, 2], [3, [8, 9]], [5, 6, 7]]
print(reverseList(inputList2[::-1]))

inputList3 = [[1, 2], [3, [8, 9]], [5, 6, 7], [10, [12, [13, 16, 17, [18, 19, [20, 21]]], 14], 15]]
print(reverseList(inputList3[::-1]))
