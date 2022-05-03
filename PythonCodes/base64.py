def createGroups(bits,number):
    output = []
    groups = int(len(number)/bits)
    for j in range(groups):
        output.append(number[0:bits])
        number = number[bits:]
    return output


def bogusElement(plaintext):
    elements = list("0123456789ABCDEF")
    plaintext = list(plaintext.upper())
    if not "0" in plaintext:
        return "0"
    else:
        for i in reversed(elements):
            if not i in plaintext:
                return i


def hexadecimalToBinary(word):
    hex_table = {'0' : "0000",
          '1' : "0001",
          '2' : "0010",
          '3' : "0011",
          '4' : "0100",
          '5' : "0101",
          '6' : "0110",
          '7' : "0111",
          '8' : "1000",
          '9' : "1001",
          'A' : "1010",
          'B' : "1011",
          'C' : "1100",
          'D' : "1101",
          'E' : "1110",
          'F' : "1111" }
    output = ""
    for i in word:
        output += hex_table[i]
    return output


def BinaryToHexadecimal(number):
    number = createGroups(4, number)
    hex_table = {"0000" : '0',
          "0001" : '1',
          "0010" : '2',
          "0011" : '3',
          "0100" : '4',
          "0101" : '5',
          "0110" : '6',
          "0111" : '7',
          "1000" : '8',
          "1001" : '9',
          "1010" : 'A',
          "1011" : 'B',
          "1100" : 'C',
          "1101" : 'D',
          "1110" : 'E',
          "1111" : 'F' }
    output = ""
    for i in number:
        output += hex_table[i]
    return output
    
    
def numToBinary(length, number):
    output = bin(number).replace("0b", "")
    return "0" * (length - len(output)) + output


def binaryToNum(number):
    return int(number,2)


def ungroup(group):
    return "".join(group)


def expansionBox(number):
    groups = createGroups(4, number)
    output = []
    for i in range(len(groups)):
        output.append(groups[(i-1)%len(groups)][3] + str(groups[i]) + groups[(i+1)%len(groups)][0])
    return "".join(output)


def xor(a,b):
    output = ""
    for i in range(len(a)):
        output += str(int(a[i])^int(b[i]))
    return output


def substitutionBox(number):
    sbox =  [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13 ]],
            
         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
           [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9 ]],
   
         [ [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
           [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
           [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12 ]],
       
          [ [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
           [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
           [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] ],
        
          [ [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
           [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
           [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3 ]],
       
         [ [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
           [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13] ],
         
          [ [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
           [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12] ],
        
         [ [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] ] ]
    output = ""
    number = createGroups(6, number)
    for i in range(8):
        row = binaryToNum(number[i][0] + number[i][-1])
        col = binaryToNum(number[i][1:-1])
        output += numToBinary(4, sbox[i][row][col])
    return output


def initialPermutation(number):
    permutation_table = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]
    
    output = ""
    for i in range(len(permutation_table)):
        output += number[permutation_table[i]-1]
    return output


def permutationChoice_1(number):
    
    permutation_table = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4 ]
    
    output = ""
    for i in range(len(permutation_table)):
        output += number[permutation_table[i] - 1]
    return output


def permutationChoice_2(number):
    permutation_table = [14, 17, 11, 24, 1, 5,
            3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8,
            16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55,
            30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53,
            46, 42, 50, 36, 29, 32 ]
    
    output = ""
    for i in range(len(permutation_table)):
        output += number[permutation_table[i] - 1]
    return output


def permutation(number):
    permutation_table = [ 16,  7, 20, 21,
        29, 12, 28, 17,
         1, 15, 23, 26,
         5, 18, 31, 10,
         2,  8, 24, 14,
        32, 27,  3,  9,
        19, 13, 30,  6,
        22, 11,  4, 25 ]
    output = ""
    for i in range(len(number)):
        output += number[permutation_table[i]-1]
    return output


def inverseInitialPermutation(number):
    
    inverse_permutation_table = [ 40, 8, 48, 16, 56, 24, 64, 32,
               39, 7, 47, 15, 55, 23, 63, 31,
               38, 6, 46, 14, 54, 22, 62, 30,
               37, 5, 45, 13, 53, 21, 61, 29,
               36, 4, 44, 12, 52, 20, 60, 28,
               35, 3, 43, 11, 51, 19, 59, 27,
               34, 2, 42, 10, 50, 18, 58, 26,
               33, 1, 41, 9, 49, 17, 57, 25 ]
    
    output = ""
    for i in range(len(number)):
        output += number[inverse_permutation_table[i]-1]
    return output
    
    
def shift_left(number,i_value):
    shift_table = [1, 1, 2, 2,
                2, 2, 2, 2,
                1, 2, 2, 2,
                2, 2, 2, 1 ]
    
    noOfShifts = shift_table[i_value]
    output = ""
    for i in range(len(number)):
        output += number[(i + noOfShifts)%len(number)]
    return output


def keys(key):
    key_list = []
    key = permutationChoice_1(key)
    left_key = key[0:28]
    right_key = key[28:]
    for i in range(16):
        left_key = shift_left(left_key,i)
        right_key = shift_left(right_key,i)
        key_list.append(permutationChoice_2(left_key + right_key))
    return key_list
    

def encryption(plaintext, key):
    if len(key)%16:
        key = key + (16 - len(key)%16)*bogusElement(key)
    if len(plaintext)%16:
        plaintext = plaintext + (16 - len(plaintext)%16)*bogusElement(plaintext)
    key = hexadecimalToBinary(key[0:16])
    plaintext = hexadecimalToBinary(plaintext)
    ciphertext = ""
    plaintext = createGroups(64, plaintext)
    for k in range(len(plaintext)):
        plaintext[k] = initialPermutation(plaintext[k])
        left = plaintext[k][0:32]
        right = plaintext[k][32:]
        temp = right
        for i in range(16):
            temp = right
            right = expansionBox(right)
            right = xor(right, keys(key)[i])
            right = substitutionBox(right)
            right = permutation(right)
            right = xor(right,left)
            left = temp
        left,right = right,left
        ciphertext += inverseInitialPermutation(left + right)
    return BinaryToHexadecimal(ciphertext)


def decryption(ciphertext, key):
    if len(key)%16:
        key = key + (16 - len(key)%16)*bogusElement(key)
    plaintext = ""
    ciphertext = hexadecimalToBinary(ciphertext)
    key = hexadecimalToBinary(key[0:16])
    ciphertext = createGroups(64, ciphertext)
    for k in range(len(ciphertext)):
        ciphertext[k] = initialPermutation(ciphertext[k])
        left = ciphertext[k][0:32]
        right = ciphertext[k][32:]
        temp = right
        for i in reversed(range(16)):
            temp = right
            right = expansionBox(right)
            right = xor(right, keys(key)[i])
            right = substitutionBox(right)
            right = permutation(right)
            right = xor(right,left)
            left = temp
        left,right = right,left
        plaintext += inverseInitialPermutation(left + right)
    return BinaryToHexadecimal(plaintext)
    

plaintext = input("Enter the text you want to Encrypt: ")
key = input("Enter the key: ")
print(f"The encrypted text is: {encryption(plaintext,key)}")
encrypted_text = input("Enter the encrypted text: ")
decryption_key = input("Enter the decryption key: ")
print(f"The decrypted text is: {decryption(encrypted_text,decryption_key)}")