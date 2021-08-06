def solution(A, K):
    # write your code in Python 3.6
    result = [0] * len(A)
    for i in range(len(A)):
        resultIndex = (i + K) % len(A)
        result[resultIndex] = A[i]
    return result


"""
Task Score
100%
Correctness
100%
Performance
Not assessed
"""
