def solution(A):
    # write your code in Python 3.6
    #return len(set(A))
    if len(A) == 0:
        return 0

    A.sort()
    result = 1
    for i in range(len(A)-1):
        if A[i] != A[i+1]:
            result += 1
    return result
"""
Task Score
100%
Correctness
100%
Performance
100%
"""
