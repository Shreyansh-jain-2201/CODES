def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return (m[0][0]*m[1][1]-m[0][1]*m[1][0])*1.0

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1.0)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def adjugate(m):
    cofactors = []
    if len(m) == 2:
        cofactors = [[m[1][1], -1*m[0][1]],
                [-1*m[1][0], m[0][0]]]
    else:
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = getMatrixMinor(m,r,c)
                cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
            cofactors.append(cofactorRow)
        cofactors = transpose(cofactors)
    for i in range(len(cofactors)):
        for j in range(len(cofactors)):
            cofactors[i][j] = int(cofactors[i][j] % 26)
    return cofactors

def inverseMatrix(matrix):
    d = 0
    d_inv = 0
    k_inv = []
    adj = adjugate(matrix)
    # print(adj)
    output = adj
    d = getMatrixDeternminant(matrix)
    d = d%26
    print(d)
    for i in range(1,26,1):
        print(i)
        if (d * i)%26 == 1:
            d_inv = i
            print(i)
            break
    k_inv = adj
    # print(k_inv, d_inv)
    for i in range(len(adj)):
        for j in range(len(adj)):
            k_inv[i][j] = int((adj[i][j] * d_inv)%26)
    return k_inv
    
    
    
    
    # for i in range(len(adj)):
    #     for j in range(len(adj)):
    #         output[i][j] = (adj[i][j]*d_inv)%26
    # return output


matrix = [[0,11,15],[7,0,1],[4,19,23]]
print(inverseMatrix(matrix))
# print(getMatrixDeternminant(matrix))