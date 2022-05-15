def MakeGrid(strArr):
    grid = []
    filler = ['x', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in str(strArr):
        if i in filler:
            grid.append(i)
    s = 81 - len(grid)
    if s:
        for i in range(s):
            grid.append('x')

    for i in range(0, len(grid), 9):
        grid.append(grid[i:i+9])
    grid = grid[-9:]
    return grid


def quadrant(strArr):
    quadrants = [[-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1], [-1]]
    for i in range(len(strArr)):
        for j in range(len(strArr)):
            if i < 3 and j < 3:
                quadrants[0].append(strArr[i][j])
            elif i < 3 and j < 6 and j >= 3:
                quadrants[1].append(strArr[i][j])
            elif i < 3 and j < 9 and j >= 6:
                quadrants[2].append(strArr[i][j])
            elif i < 6 and i >= 3 and j < 3:
                quadrants[3].append(strArr[i][j])
            elif i < 6 and i >= 3 and j < 6 and j >= 3:
                quadrants[4].append(strArr[i][j])
            elif i < 6 and i >= 3 and j < 9 and j >= 6:
                quadrants[5].append(strArr[i][j])
            elif i < 9 and i >= 6 and j < 3:
                quadrants[6].append(strArr[i][j])
            elif i < 9 and i >= 6 and j < 6 and j >= 3:
                quadrants[7].append(strArr[i][j])
            elif i < 9 and i >= 6 and j < 9 and j >= 6:
                quadrants[8].append(strArr[i][j])
        quadrants[i] = quadrants[i][1:]
    return quadrants


def checkRepeatation(strArr):
    strArr = MakeGrid(strArr)
    indices = []
    output = []
    for i in range(len(strArr)):
        temp = []
        for j in range(len(strArr)):
            if strArr[i][j] in temp and strArr[i][j] != 'x':
                indices.append([i, temp.index(strArr[i][j])])
                indices.append([i, j])
            temp.append(strArr[i][j])
    for i in indices:
        if i not in output:
            output.append(i)
    return output


def makeRows(strArr):
    return [[row[i] for row in strArr] for i in range(len(strArr[0]))]


def MatrixChallenge(strArr):
    grid = []
    subgrids = []
    strArr = MakeGrid(strArr)
    grid = checkRepeatation(strArr)
    if checkRepeatation(makeRows(strArr)) != None:
        for i in checkRepeatation(makeRows(strArr)):
            grid.append([i[1], i[0]])
    if checkRepeatation(quadrant(strArr)) != None:
        for i in checkRepeatation(quadrant(strArr)):
            subgrids.append(i[0] + 1)
    for k in range(len(grid)):
        if grid[k] not in subgrids:
            i, j = grid[k][0], grid[k][1]
            if i < 3 and j < 3:
                subgrids.append(1)
            elif i < 3 and j < 6:
                subgrids.append(2)
            elif i < 3 and j < 9:
                subgrids.append(3)
            elif i < 6 and j < 3:
                subgrids.append(4)
            elif i < 6 and j < 6:
                subgrids.append(5)
            elif i < 6 and j < 9:
                subgrids.append(6)
            elif i < 9 and j < 3:
                subgrids.append(7)
            elif i < 9 and j < 6:
                subgrids.append(8)
            else:
                subgrids.append(9)
    if len(subgrids) == 0:
        return "legal"
    output = ''
    l = list(set(subgrids))
    l.sort()
    for i in l:
        output += str(i) + ", "
    return output[0:-2]


strArr = str([[1, 2, 3, 4, 5, 6, 7, 8, 9],
              ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']])
print(MatrixChallenge(strArr))
