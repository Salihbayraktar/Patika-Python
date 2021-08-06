def maze_runner(maze, directions):
    # Code Here
    m = len(maze)
    n = len(maze[0])
    mPosition = 0
    nPosition = 0
    control = False
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 2:
                mPosition = i
                nPosition = j
                control = True
                break
        if control:
            break
    for i in directions:
        if i == 'N':
            mPosition -= 1
        elif i == 'S':
            mPosition += 1
        elif i == 'E':
            nPosition += 1
        else:
            nPosition -= 1
        if mPosition >= m or mPosition < 0 or nPosition >= n or nPosition < 0 or maze[mPosition][nPosition] == 1:
            return "Dead"
        elif maze[mPosition][nPosition] == 3:
            return "Finish"
    return "Lost"
