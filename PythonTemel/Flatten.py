def flatten(inputList, flattenList):
    if type(inputList) != type([]):
        flattenList.append(inputList)
        return

    for i in inputList:
        if type(inputList) == type([]):
            flatten(i, flattenList)

    return flattenList


inputList = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
flattenListSpare = []
flattenList = flatten(inputList, flattenListSpare)

print(flattenList)