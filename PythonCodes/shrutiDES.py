# DES Shruti

def num_to_bin(length, num):
    op = bin(num).replace("0b", "")
    return "0" * (length - len(op)) + op


def bin_to_num(num):
    return int(num, 2)


def hex_to_bin(word):
    ht = {'0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100", '5': "0101", '6': "0110", '7': "0111",
          '8': "1000", '9': "1001", 'A': "1010", 'B': "1011", 'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}
    op = ""
    for i in word:
        op += ht[i]
    return op


def bin_to_hex(num):
    num = make_groups(4, num)
    ht = {"0000": '0',
          "0001": '1',
          "0010": '2',
          "0011": '3',
          "0100": '4',
          "0101": '5',
          "0110": '6',
          "0111": '7',
          "1000": '8',
          "1001": '9',
          "1010": 'A',
          "1011": 'B',
          "1100": 'C',
          "1101": 'D',
          "1110": 'E',
          "1111": 'F'}
    op = ""
    for i in num:
        op += ht[i]
    return op


def make_groups(bits, num):
    op = []
    groups = int(len(num)/bits)
    for j in range(groups):
        op.append(num[0:bits])
        num = num[bits:]
    return op


def ungroup(group):
    return "".join(group)


def filler_letter(pt):
    elements = list("0123456789ABCDEF")
    pt = list(pt.upper())
    if not "0" in pt:
        return "0"
    else:
        for i in reversed(elements):
            if not i in pt:
                return i


def substitution_box(num):
    sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
             [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
             [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
             [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

            [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
             [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
             [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
             [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

            [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
             [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
             [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
             [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

            [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

            [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

            [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
             [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
             [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
             [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

            [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

            [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
             [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
             [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
             [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
    op = ""
    num = make_groups(6, num)
    for i in range(8):
        row = bin_to_num(num[i][0] + num[i][-1])
        col = bin_to_num(num[i][1:-1])
        op += num_to_bin(4, sbox[i][row][col])
    return op


def expansion_box(num):
    groups = make_groups(4, num)
    op = []
    for i in range(len(groups)):
        op.append(groups[(i-1) % len(groups)][3] +
                  str(groups[i]) + groups[(i+1) % len(groups)][0])
    return "".join(op)


def xor(a, b):
    op = ""
    for i in range(len(a)):
        op += str(int(a[i]) ^ int(b[i]))
    return op


def initial_permutation(num):
    permutation_table = [58, 50, 42, 34, 26, 18, 10, 2,
                         60, 52, 44, 36, 28, 20, 12, 4,
                         62, 54, 46, 38, 30, 22, 14, 6,
                         64, 56, 48, 40, 32, 24, 16, 8,
                         57, 49, 41, 33, 25, 17, 9, 1,
                         59, 51, 43, 35, 27, 19, 11, 3,
                         61, 53, 45, 37, 29, 21, 13, 5,
                         63, 55, 47, 39, 31, 23, 15, 7]

    op = ""
    for i in range(len(permutation_table)):
        op += num[permutation_table[i]-1]
    return op


def pc_1(num):

    permutation_table = [57, 49, 41, 33, 25, 17, 9,
                         1, 58, 50, 42, 34, 26, 18,
                         10, 2, 59, 51, 43, 35, 27,
                         19, 11, 3, 60, 52, 44, 36,
                         63, 55, 47, 39, 31, 23, 15,
                         7, 62, 54, 46, 38, 30, 22,
                         14, 6, 61, 53, 45, 37, 29,
                         21, 13, 5, 28, 20, 12, 4]

    op = ""
    for i in range(len(permutation_table)):
        op += num[permutation_table[i] - 1]
    return op


def pc_2(num):
    permutation_table = [14, 17, 11, 24, 1, 5,
                         3, 28, 15, 6, 21, 10,
                         23, 19, 12, 4, 26, 8,
                         16, 7, 27, 20, 13, 2,
                         41, 52, 31, 37, 47, 55,
                         30, 40, 51, 45, 33, 48,
                         44, 49, 39, 56, 34, 53,
                         46, 42, 50, 36, 29, 32]

    op = ""
    for i in range(len(permutation_table)):
        op += num[permutation_table[i] - 1]
    return op


def permutation(num):
    permutation_table = [16,  7, 20, 21,
                         29, 12, 28, 17,
                         1, 15, 23, 26,
                         5, 18, 31, 10,
                         2,  8, 24, 14,
                         32, 27,  3,  9,
                         19, 13, 30,  6,
                         22, 11,  4, 25]
    op = ""
    for i in range(len(num)):
        op += num[permutation_table[i]-1]
    return op


def inverse_initial_permutation(num):

    inverse_permutation_table = [40, 8, 48, 16, 56, 24, 64, 32,
                                 39, 7, 47, 15, 55, 23, 63, 31,
                                 38, 6, 46, 14, 54, 22, 62, 30,
                                 37, 5, 45, 13, 53, 21, 61, 29,
                                 36, 4, 44, 12, 52, 20, 60, 28,
                                 35, 3, 43, 11, 51, 19, 59, 27,
                                 34, 2, 42, 10, 50, 18, 58, 26,
                                 33, 1, 41, 9, 49, 17, 57, 25]

    op = ""
    for i in range(len(num)):
        op += num[inverse_permutation_table[i]-1]
    return op


def shift_left(num, i_value):
    shift_table = [1, 1, 2, 2,
                   2, 2, 2, 2,
                   1, 2, 2, 2,
                   2, 2, 2, 1]

    noOfShifts = shift_table[i_value]
    op = ""
    for i in range(len(num)):
        op += num[(i + noOfShifts) % len(num)]
    return op


def keys(key):
    key_list = []
    key = pc_1(key)
    left_key = key[0:28]
    right_key = key[28:]
    for i in range(16):
        left_key = shift_left(left_key, i)
        right_key = shift_left(right_key, i)
        key_list.append(pc_2(left_key + right_key))
    return key_list


def encryption(pt, key):
    if len(pt) % 16:
        pt = pt + (16 - len(pt) % 16)*filler_letter(pt)
    if len(key) % 16:
        key = key + (16 - len(key) % 16)*filler_letter(key)
    key = hex_to_bin(key[0:16])
    pt = hex_to_bin(pt)
    ciphertext = ""
    pt = make_groups(64, pt)
    for k in range(len(pt)):
        pt[k] = initial_permutation(pt[k])
        left = pt[k][0:32]
        right = pt[k][32:]
        temp = right
        for i in range(16):
            temp = right
            right = expansion_box(right)
            right = xor(right, keys(key)[i])
            right = substitution_box(right)
            right = permutation(right)
            right = xor(right, left)
            left = temp
        left, right = right, left
        ciphertext += inverse_initial_permutation(left + right)
    return bin_to_hex(ciphertext)


def decryption(ciphertext, key):
    if len(key) % 16:
        key = key + (16 - len(key) % 16)*filler_letter(key)
    pt = ""
    ciphertext = hex_to_bin(ciphertext)
    key = hex_to_bin(key[0:16])
    ciphertext = make_groups(64, ciphertext)
    for k in range(len(ciphertext)):
        ciphertext[k] = initial_permutation(ciphertext[k])
        left = ciphertext[k][0:32]
        right = ciphertext[k][32:]
        temp = right
        for i in reversed(range(16)):
            temp = right
            right = expansion_box(right)
            right = xor(right, keys(key)[i])
            right = substitution_box(right)
            right = permutation(right)
            right = xor(right, left)
            left = temp
        left, right = right, left
        pt += inverse_initial_permutation(left + right)
    return bin_to_hex(pt)


pt = input("Enter the plaintext: ")
key = input("Enter the key: ")
print(f"The ciphertext is: {encryption(pt,key)}")
encrypted_text = input("Enter the ciphertext: ")
decryption_key = input("Enter the decryption key: ")
print(f"The decrypted text is: {decryption(encrypted_text,decryption_key)}")
