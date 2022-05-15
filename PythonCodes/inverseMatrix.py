def determinant(matrix,order):
    d = 0
    if order == 2:
        d = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    elif order == 3:
        d = matrix[0][0]*(matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1]) - 




matrix = [[6,24,1][13,16,10][20,17,15]]
