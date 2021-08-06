#print(solution(6, 11, 2))
#print(solution(0, 1, 11))

# approach 4
"""
def prefixSum(A,B,K):
    prefixSumA = [0] * ((B // K) + 2)
    prefixSumA[0] = 1
    j = 1
    for i in range(0, B+1, K):
        prefixSumA[j] = prefixSumA[j-1] + 1
        j += 1
    return prefixSumA


def solution(A, B, K):
    prefixSumA = prefixSum(A,B,K)
    leftIndex = A // K
    rightIndex = B // K
    result = prefixSumA[rightIndex] - prefixSumA[leftIndex]
    divideA = 1 if A % K == 0 else 0
    return result + divideA
"""
"""
Task Score
62%
Correctness
100%
Performance
25%
"""


# approach 3
"""
def solution(A, B, K):
    if B == K or (A == 0 and B < K):
        return 1
    elif (A == B and B % K != 0) or B < K:
        return 0
    else:
        if A % K == 0 or B % K == 0 or (A <= K <= B):
            return ((B - A) // K) + 1
        else:
            return (B - A) // K

"""
"""
Task Score
75%
Correctness
100%
Performance
50%    
"""


# approach 2
"""
def solution(A, B, K):
    if B == K:
        return 1
    elif (A == B and B != K) or B < K:
        return 0
    else:
        if A % K == 0 or B % K == 0:
            return ((B - A) // K) + 1
        else:
            return (B - A) // K

"""
"""
Task Score
37%
Correctness
25%
Performance
50%
"""


#approach 1
"""
def solution(A, B, K):
    # write your code in Python 3.6
    return ((B - A) // K ) + 1
"""
"""
Task Score
50%
Correctness
25%
Performance
75%
"""
