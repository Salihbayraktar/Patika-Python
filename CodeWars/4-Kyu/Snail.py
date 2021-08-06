def snail(snail_map):
    lineNumber = (len(snail_map) * 2) - 1
    result = []
    maxM = len(snail_map)
    maxN = len(snail_map[0])
    move = 'E'
    currentM = 0
    currentN = 0
    for _ in range(lineNumber):
        if move == 'E':
            for _ in range(maxN):
                result.append(snail_map[currentM][currentN])
                currentN += 1
            currentN -= 1
            currentM += 1
            maxM -= 1
            move = 'S'
        elif move == 'S':
            for _ in range(maxM):
                result.append(snail_map[currentM][currentN])
                currentM += 1
            currentM -= 1
            currentN -= 1
            maxN -= 1
            move = 'W'
        elif move == 'W':
            for _ in range(maxN):
                result.append(snail_map[currentM][currentN])
                currentN -= 1
            currentN += 1
            currentM -= 1
            maxM -= 1
            move = 'N'
        elif move == 'N':
            for _ in range(maxM):
                result.append(snail_map[currentM][currentN])
                currentM -= 1
            currentM += 1
            currentN += 1
            maxN -= 1
            move = 'E'
    return result


array = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print(snail(array))
