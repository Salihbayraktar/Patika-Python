def solution(A):
    # write your code in Python 3.6

    B = set(A)
    lastFoundedNumber = 1
    for _ in B:
        if lastFoundedNumber in B:
            lastFoundedNumber += 1
            continue
        else:
            return lastFoundedNumber
    return lastFoundedNumber


A = [0, 2, 4, 6, 7, 9, 0, 0, 1, 3, 5, 7, 9]
# A = list(range(1_000_000))
# print(A)
print(solution(A))

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
    A.sort()
    for i in range(len(A)-1):
        if A[i] + 1 == A[i+1] or A[i] == A[i+1]:
            continue
        else:
            return A[i] + 1 if A[i] >= 0 else 1
    return A[len(A)-1] + 1 if A[len(A)-1] >= 0 else 1
    
    Task Score
    33%
    Correctness
    20%
    Performance
    50%
"""
