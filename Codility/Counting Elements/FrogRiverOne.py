def solution(X, A):
    dictionary = {}
    for i in range(len(A)):
        if dictionary.get(A[i]) is None:
            dictionary[A[i]] = i
    reqSec = 0
    for i in range(1, X + 1):
        try:
            if dictionary[i] > reqSec:
                reqSec = dictionary[i]
        except Exception:
            return -1
    return reqSec


print(solution(5, [1, 5, 7, 9, 15, 35, 1, 5, 7, 9, 29, 31, 566, 2, 3, 4]))

"""
Task Score
100%
Correctness
100%
Performance
100%
"""



""" 
def solution(X, A):      
    reqSec = 0
    for i in range(1, X + 1):
        try:
            index = A.index(i)
            if index > reqSec:
                reqSec = index
        except ValueError:
            return -1

    return reqSec
"""