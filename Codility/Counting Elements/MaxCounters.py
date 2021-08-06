def solution(N, A):
    maxCounter = 0
    resultList = [0] * N
    for i in A:
        index = i - 1
        if index != N:
            resultList[index] += 1
            if resultList[index] > maxCounter:
                maxCounter = resultList[index]
        else:
            resultList = [maxCounter] * N
    return resultList


N = 5
A = [3, 4, 4, 6, 1, 4, 4, 5, 6, 1, 3, 5, 2, 2, 2, 2, 6]

print(solution(N, A))
"""
Task Score
88%
Correctness
100%
Performance
80%
"""
