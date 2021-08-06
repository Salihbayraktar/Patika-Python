"""

Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.


lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
"""


def lone_sum(a, b, c):
    sum = 0
    if a != b and a != c:
        sum += a
    if b != a and b != c:
        sum += b
    if c != a and c != b:
        sum += c

    return sum

"""
def lone_sum(a, b, c):
    if a != b and a != c and b != c:
        return a + b + c
    elif a == b and a != c:
        return c
    elif a == c and a != b:
        return b
    elif b == c and b != a:
        return a
    elif a == b and b == c:
        return 0
    else:
        return b + c
"""