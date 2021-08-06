def solution(A):
    # write your code in Python 3.6
    A.sort()
    checkNumber = 1
    for i in range(len(A)):
        if checkNumber == A[i]:
            checkNumber += 1
        else:
            return 0
    return 1
"""
Task Score
100%
Correctness
100%
Performance
100%
"""


"""
def solution(A):
    # write your code in Python 3.6
    A.sort()
    for i in range(len(A)-1):
        if A[i] + 1 != A[i+1]:
            return 0
    return 1

Task Score
66%
Correctness
33%
Performance
100%
"""