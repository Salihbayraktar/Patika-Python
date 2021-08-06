def fibonacciSum(n):
    fib = 1
    fibPrev = 1
    sum = 2
    for i in range(n - 1):
        value = fib
        fib += fibPrev
        fibPrev = value
        sum += fib
    return sum


def perimeter(n):
    return 4 * fibonacciSum(n)
