def prefixSum(A):
    prefixSumA = [0] * len(A)
    prefixSumA[0] = A[0]
    for i in range(1, len(A)):
        prefixSumA[i] = prefixSumA[i - 1] + A[i]
    return prefixSumA


def solution(A):
    prefixSumA = prefixSum(A)
    count = 0
    for i in range(len(A)):
        if A[i] == 0:
            count += prefixSumA[len(A) - 1] - prefixSumA[i]
            if count > 1000000000:
                return -1
    return count

"""
Task Score
100%
Correctness
100%
Performance
100%
"""

A = [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0,
     0, 1, 0, 0, 1]
print(solution(A))
print(len(A))
