def solution(A):
    # write your code in Python 3.6
    if len(A) == 0:
        return 1
    A.sort()
    if(A[0] == 2):
        return 1
    for i in range(len(A)-1):
        if A[i] + 1 == A[i+1]:
            continue
        else:
            return A[i] + 1
    return A[len(A)-1] + 1

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
        if A[i] + 1 == A[i+1]:
            continue
        else:
            return  A[i] + 1
    return A[len(A)-1] + 1

    Task Score
    50%
    Correctness
    20%
    Performance
    80%
"""


"""
def solution(A):
    A.sort()
    if(A[0] == 2):
        return 1
    for i in range(len(A)-1):
        if A[i] + 1 == A[i+1]:
            continue
        else:
            return A[i] + 1
    return A[len(A)-1] + 1
    
    Task Score
    90%
    Correctness
    80%
    Performance
    100%
"""



