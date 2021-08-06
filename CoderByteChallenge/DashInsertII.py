def DashInsertII(num):
    resultList = []
    numStr = str(num)
    for i in range(len(numStr) - 1):
        if int(numStr[i]) == 0 or int(numStr[i + 1]) == 0:
            resultList.append(numStr[i])
        elif int(numStr[i]) % 2 == 0 and int(numStr[i + 1]) % 2 == 0:
            resultList.append(numStr[i])
            resultList.append('*')
        elif int(numStr[i]) % 2 == 1 and int(numStr[i + 1]) % 2 == 1:
            resultList.append(numStr[i])
            resultList.append('-')
        else:
            resultList.append(numStr[i])
    resultList.append(numStr[len(numStr) - 1])
    return ''.join(resultList)


# keep this function call here
print(DashInsertII(input()))
