def solution(A):
    if len(A) == 1:
        return A[0]

    A.sort()
    counter = 1
    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            counter += 1
        else:
            if counter % 2 == 1:
                return A[i]
            else:
                counter = 1
    return A[len(A)-1]


A = [9, 3, 9, 3, 9, 7, 9]
print(solution(A))

"""
Task Score
100%
Correctness
100%
Performance
100%
"""
