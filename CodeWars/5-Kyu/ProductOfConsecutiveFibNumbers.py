def productFib(prod):
    firstFib = 0
    secondFib = 1
    multiplication = firstFib * secondFib
    while multiplication < prod:
        value = firstFib
        firstFib = secondFib
        secondFib += value
        multiplication = firstFib * secondFib

    result = True if multiplication == prod else False
    return [firstFib, secondFib, result]
