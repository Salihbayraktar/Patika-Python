def solution(N):

    maxGap = 0
    currentGap = 0
    is_find_one = False
    while N != 0:
        if N % 2 == 1 and is_find_one == False:
            is_find_one = True
        elif N % 2 == 1 and is_find_one:
            if currentGap > maxGap:
                maxGap = currentGap
            currentGap = 0
        elif N % 2 == 0 and is_find_one:
            currentGap += 1
        N = N // 2
    return maxGap

"""
Task Score
100%
Correctness
100%
Performance
Not assessed
"""