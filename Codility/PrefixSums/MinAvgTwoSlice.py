def prefixSum(A):
    prefixSumA = [0] * (len(A) + 1)
    prefixSumA[1] = A[0]
    for i in range(2, len(A) + 1):
        prefixSumA[i] = prefixSumA[i - 1] + A[i - 1]
    return prefixSumA


def solution(A):
    prefixSumA = prefixSum(A)
    minSliceSum = (A[0] + A[1]) / 2
    minSumStartIndex = 0
    sliceCounter = 0
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            sliceSum = (prefixSumA[j + 1] - prefixSumA[i]) / (j - i + 1)
            sliceCounter += 1
            if sliceCounter > 5:
                sliceCounter = 0
                break
            if sliceSum < minSliceSum:
                minSliceSum = sliceSum
                minSumStartIndex = i
    return minSumStartIndex

"""
Task Score
90%
Correctness
80%
Performance
100%
"""


A = [4, 2, 2, 5, 1, 5, 8]
B = [0,1,2,3,4,5,6,7,8,9] * 10000
print(solution(A))
print(solution(B))
