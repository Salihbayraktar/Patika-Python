def solution(A):
    # write your code in Python 3.6
    A.sort()
    return max((A[len(A) - 1] * A[len(A) - 2] * A[len(A) - 3]), (A[len(A) - 1] * A[0] * A[1]))


"""
Task Score
100%
Correctness
100%
Performance
100%
"""

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 10000
print(solution(A))
print(len(A))
