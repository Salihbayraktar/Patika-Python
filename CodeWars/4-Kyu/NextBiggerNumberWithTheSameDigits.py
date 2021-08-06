def next_bigger(n):
    if len(str(n)) == 0 or len(str(n)) == 1:
        return -1

    strN = str(n)
    numbers = []
    nextSmallNumber = 0
    nextSmallNumberIndex = 0

    for i in range(len(strN) - 1, 0, -1):

        numbers.append(int(strN[i]))

        if int(strN[i]) > int(strN[i - 1]):
            numbers.append(int(strN[i - 1]))
            nextSmallNumber = int(strN[i - 1])
            nextSmallNumberIndex = i - 1
            break

        if i == 1:
            return -1

    numbers.sort()
    smallestBigNumber = 0

    for i in numbers:
        if i > nextSmallNumber:
            smallestBigNumber = i
            numbers.remove(i)
            break

    result = strN[:nextSmallNumberIndex] + str(smallestBigNumber)

    for i in numbers:
        result += str(i)
    return int(result)


n = 8189640851753
print(next_bigger(n))
"""
8429098  57550  #my answer (wrong)
8429098  55750  #question
8429098  57055  #true answer

"""
