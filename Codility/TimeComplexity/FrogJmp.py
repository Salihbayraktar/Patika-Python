def solution(X, Y, D):
    # write your code in Python 3.6
    if (Y - X) / D % 1 == 0:
        return  (Y - X) // D
    else:
        return  (Y - X) // D + 1

"""
Task Score
100%
Correctness
100%
Performance
100%
"""