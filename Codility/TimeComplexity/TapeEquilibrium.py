def solution(A):
    # write your code in Python 3.6


    sumA = sum(A)
    leftSum = A[0]
    minDiff = abs(2*leftSum - sumA)
    for i in range(1, len(A)):
        leftSum += A[i]
        difference = abs(2*leftSum - sumA)
        if difference < minDiff:
            minDiff = difference
    return minDiff

"""
Task Score
84%
Correctness
71%
Performance
100%
"""



"""
def solution(A):    
    sumA = sum(A)
    minDiff = abs(A[0] - (sumA - A[0]))
    for i in range(1,len(A)):
        leftSum = sum(A[:i])
        difference = abs(leftSum - (sumA- leftSum))
        if difference < minDiff:
            minDiff = difference
            if minDiff == 0:
                return 0
    return minDiff
"""