def zeros(n):
    count5 = 0
    spareN = n
    while spareN != 0:
        count5 += spareN // 5
        spareN = spareN // 5
    spareN = n
    return count5


n = 150
print(zeros(150))