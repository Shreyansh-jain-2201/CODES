# Hill Cipher

def bogusElement(plaintext):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    plaintext = list(plaintext.upper())
    if not "X" in plaintext:
        return "X"
    else:
        for i in reversed(alphabets):
            if not i in plaintext:
                return i
   
    
def createPair(plaintext,key):
    bogus = bogusElement(plaintext)
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(" ", "")
    num = 0 
    for i in range(len(key)):
        if i**2 >= len(key):
            num = i
            break
    while len(plaintext)%num != 0:
        plaintext += bogus
    output = []
    for i in range(0,len(plaintext),num):
        try:
            list2 = []
            for j in range(num):
                list2.append(plaintext[i+j])
            output.append(list2)
        except:
            continue
    return output


def createKeyPairs(key):
    bogus = bogusElement(key)
    key = key.upper()
    key = key.replace(" ", "")
    num = 0
    n = 0
    for i in range(len(key)):
        if i**2 >= len(key):
            n = i
            num = i**2
            break
    while len(key)%num != 0:
        key += bogus
    output = []
    for i in range(0,len(key),n):
        try:
            list2 = []
            for j in range(n):
                list2.append(key[i+j])
            output.append(list2)
        except:
            continue
    return output


def Matrix(pairs):
    output = []
    alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for pair in pairs:
        list1 = []
        for i in range(len(pair)):
            list1.append(alphabets.index(pair[i]))
        output.append(list1)
    return output


def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def getMatrixDeternminant(m):

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
    d_inv = -1
    k_inv = []
    adj = adjugate(matrix)
    output = adj
    d = getMatrixDeternminant(matrix)
    d = d%26
    for i in range(26):
        if (d * i)%26 == 1:
            d_inv = i
    if d_inv == -1:
        return -1
    else:
        k_inv = adj
        for i in range(len(adj)):
            for j in range(len(adj)):
                k_inv[i][j] = int((adj[i][j] * d_inv)%26)
    return k_inv


def encrypt(plaintext,key):
    bogus = bogusElement(plaintext)
    key_pairs = createKeyPairs(key)
    key_matrix = Matrix(key_pairs)
    plaintext_pairs = createPair(plaintext,key)
    plaintext_matrix = Matrix(plaintext_pairs)
    alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    output = ""
    for pair in plaintext_matrix:
        for j in range(len(pair)):
            n = 0
            for i in range(len(pair)):
                n += pair[i] * key_matrix[j][i]
            output += alphabets[n%26]
            
    return output

    
def checkKey(key):
    if inverseMatrix(Matrix(createKeyPairs(key))) == -1:
        return False
    else:
        return True
    

def decrypt(ciphertext,key):
    bogus = bogusElement(ciphertext)
    key_inverse = inverseMatrix(Matrix(createKeyPairs(key)))
    ciphertext_matrix = Matrix(createPair(ciphertext,key))
    num = len(ciphertext_matrix)
    alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    output = ""
    for pair in ciphertext_matrix:
        for j in range(len(pair)):
            n = 0
            for i in range(len(pair)):
                n += pair[i] * key_inverse[j][i]
            output += alphabets[n%26]
            
    return output


plaintext = input("Enter the text you want to Encrypt: ")
key = input("Enter the key: ")
while (not checkKey(key)):
    print("The key you entered is invalid. Please try again.")
    key = input("Enter the key: ")
print(f"The encrypted text is: {encrypt(plaintext,key)}")

encrypted_text = input("Enter the encrypted text: ")
decryption_key = input("Enter the decryption key: ")
while (not checkKey(decryption_key)):
    print("The key you entered is invalid. Please try again.")
    decryption_key = input("Enter the decryption key: ")
print(f"The decrypted text is: {decrypt(encrypted_text,decryption_key)}")

