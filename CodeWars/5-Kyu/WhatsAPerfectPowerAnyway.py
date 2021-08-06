def isPP(n):
    halfN = n // 2
    for i in range(2, halfN + 1):
        counter = 1
        multiplacation = i
        while multiplacation < n:
            multiplacation *= i
            counter += 1
        if multiplacation == n:
            return [i, counter]
    return None
