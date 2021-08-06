def solution(S, P, Q):
    # write your code in Python 3.6
    result = []
    for i in range(len(P)):
        subStr = S[P[i]:Q[i]+1]
        if 'A' in subStr:
            result.append(1)
        elif 'C' in subStr:
            result.append(2)
        elif 'G' in subStr:
            result.append(3)
        else:
            result.append(4)
    return result
"""
Task Score
100%
Correctness
100%
Performance
100%
"""

S = 'CAGCCTAAC'
P = [1,2,4]
Q = [5,2,6]
print(solution(S, P, Q))
"""
def solution(S, P, Q):
    # write your code in Python 3.6
    S = S.replace('A', '1')
    S = S.replace('C', '2')
    S = S.replace('G', '3')
    S = S.replace('T', '4')
    print(S)

    K = len(P)
    result = []
    minNumber = 5
    for i in range(K):
        for j in range(P[i], Q[i] + 1):
            currentNumber = int(S[j])
            if currentNumber < minNumber:
                minNumber = currentNumber
                #if minNumber == 1:
                    #result.append(1)
                    #break
        #if minNumber != 1:
        result.append(minNumber)
        minNumber = 5

    return result

"""
"""
Task Score
62%
Correctness
100%
Performance
0%
"""


