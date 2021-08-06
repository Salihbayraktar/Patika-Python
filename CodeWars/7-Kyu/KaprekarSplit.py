def kaprekar_split(n):
    nSquare = str(n * n)
    if int(nSquare) == n:
        return 0
    for i in range(1, len(nSquare)):
        leftSide = int(nSquare[:i])
        rightSide = int(nSquare[i:])
        if leftSide + rightSide == n:
            return i
    return -1
