def SwapII(strParam):
    strParam = strParam.swapcase()
    words = strParam.split(' ')
    for i in range(len(words)):
        charCounter = 0
        firstNumIndex = -1
        secNumIndex = -1
        for j in range(len(words[i])):
            if words[i][j].isdigit() and firstNumIndex == -1:
                firstNumIndex = j
                charCounter = 0
            elif words[i][j].isdigit() and firstNumIndex != -1:
                secNumIndex = j
                if charCounter !=0:
                    ListI = list(words[i])
                    ListI[firstNumIndex], ListI[secNumIndex] = ListI[secNumIndex], ListI[firstNumIndex]
                    words[i] = ''.join(ListI)
                firstNumIndex = -1
                secNumIndex = -1
                charCounter = 0
            elif words[i][j].isalpha():
                charCounter += 1
    return ' '.join(words)

# keep this function call here
print(SwapII(input()))