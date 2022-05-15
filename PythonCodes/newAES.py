# AES
import base64


def createGroups(bits, number):
    output = []
    print(4, len(number))
    groups = int(len(number)/bits)
    print(5, groups)
    for j in range(groups):
        output.append(number[0:bits])
        number = number[bits:]
    print(output)
    return output


def bogusElement(plaintext):
    return "0"


def binaryToString(number):
    output = ""
    for i in range(0, len(number), 7):
        output = output + chr(int(number[i:i + 7], 2))
    return output


def BinaryToHexadecimal(number):
    number = createGroups(4, number)
    hex_table = {
        "0000": '0',
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
        "1111": 'F'
    }
    output = ""
    for i in number:
        output += hex_table[i]
    return output


def createInputMatrix(plaintext):
    hex_text = ""
    output = []
    print(9, len(plaintext))

    if len(plaintext) % 32:
        plaintext += (32 - len(plaintext) % 16)*bogusElement(plaintext)
    print(10, plaintext)
    # print(plaintext)
    plaintexts = createGroups(32, plaintext)
    # print("hello")
    for plaintext in plaintexts:
        plaintext_matrix = [[0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0],
                            [0, 0, 0, 0]]
        hex_text = ""
        for i in plaintext:
            hex_text += i
        for i in range(4):
            for j in range(4):
                plaintext_matrix[j][i] = hex_text[0:2]
                hex_text = hex_text[2:]
        output.append(plaintext_matrix)
    return output


def hexadecimalToBinary(word):
    word = word.upper()
    hex_table = {'0': "0000",
                 '1': "0001",
                 '2': "0010",
                 '3': "0011",
                 '4': "0100",
                 '5': "0101",
                 '6': "0110",
                 '7': "0111",
                 '8': "1000",
                 '9': "1001",
                 'A': "1010",
                 'B': "1011",
                 'C': "1100",
                 'D': "1101",
                 'E': "1110",
                 'F': "1111"}

    output = ""
    for i in word:
        output += hex_table[i]
    return output


def stringToHex(word):
    wordToHex = {'A': 'F0', 'B': 'F1', 'C': 'F2', 'D': 'F3', 'E': 'F4', 'F': 'F5', 'G': 'F6',
                 'H': 'F7', 'I': 'F8', 'J': 'F9', 'K': 'FA', 'L': 'FB', 'M': 'FC', 'N': 'FD',
                 'O': 'FE', 'P': 'FF', 'Q': 'E0', 'R': 'E1', 'S': 'E2', 'T': 'E3', 'U': 'E4',
                 'V': 'E5', 'W': 'E6', 'X': 'E7', 'Y': 'E8', 'Z': 'E9', 'a': 'EA', 'b': 'EB',
                 'c': 'EC', 'd': 'ED', 'e': 'EE', 'f': 'EF', 'g': 'D0', 'h': 'D1', 'i': 'D2',
                 'j': 'D3', 'k': 'D4', 'l': 'D5', 'm': 'D6', 'n': 'D7', 'o': 'D8', 'p': 'D9',
                 'q': 'DA', 'r': 'DB', 's': 'DC', 't': 'DD', 'u': 'DE', 'v': 'DF', 'w': 'C0',
                 'x': 'C1', 'y': 'C2', 'z': 'C3', '.': 'C4', ',': 'C5', '!': 'C6', '@': 'C7',
                 '#': 'C8', '$': 'C9', '%': 'CA', '^': 'CB', '&': 'CC', '*': 'CD', '(': 'CE',
                 ')': 'CF', '-': 'B0', '_': 'B1', '+': 'B2', '=': 'B3', '}': 'B4', '{': 'B5',
                 '[': 'B6', ']': 'B7', ';': 'B8', ':': 'B9', "'": 'BA', '"': 'BB', '?': 'BC',
                 '/': 'BD', ' ': '00', '1': 'BF', '2': 'A0', '3': 'A1', '4': 'A2', '5': 'A3',
                 '6': 'A4', '7': 'A5', '8': 'A6', '9': 'A7', '0': 'A8'}

    output = ""
    for i in word:
        output += wordToHex.get(i)
    return output


def HexToString(word):

    HexToWord = {'F0': 'A', 'F1': 'B', 'F2': 'C', 'F3': 'D', 'F4': 'E', 'F5': 'F', 'F6': 'G',
                 'F7': 'H', 'F8': 'I', 'F9': 'J', 'FA': 'K', 'FB': 'L', 'FC': 'M', 'FD': 'N',
                 'FE': 'O', 'FF': 'P', 'E0': 'Q', 'E1': 'R', 'E2': 'S', 'E3': 'T', 'E4': 'U',
                 'E5': 'V', 'E6': 'W', 'E7': 'X', 'E8': 'Y', 'E9': 'Z', 'EA': 'a', 'EB': 'b',
                 'EC': 'c', 'ED': 'd', 'EE': 'e', 'EF': 'f', 'D0': 'g', 'D1': 'h', 'D2': 'i',
                 'D3': 'j', 'D4': 'k', 'D5': 'l', 'D6': 'm', 'D7': 'n', 'D8': 'o', 'D9': 'p',
                 'DA': 'q', 'DB': 'r', 'DC': 's', 'DD': 't', 'DE': 'u', 'DF': 'v', 'C0': 'w',
                 'C1': 'x', 'C2': 'y', 'C3': 'z', 'C4': '.', 'C5': ',', 'C6': '!', 'C7': '@',
                 'C8': '#', 'C9': '$', 'CA': '%', 'CB': '^', 'CC': '&', 'CD': '*', 'CE': '(',
                 'CF': ')', 'B0': '-', 'B1': '_', 'B2': '+', 'B3': '=', 'B4': '}', 'B5': '{',
                 'B6': '[', 'B7': ']', 'B8': ';', 'B9': ':', 'BA': "'", 'BB': '"', 'BC': '?',
                 'BD': '/', '00': ' ', 'BF': '1', 'A0': '2', 'A1': '3', 'A2': '4', 'A3': '5',
                 'A4': '6', 'A5': '7', 'A6': '8', 'A7': '9', 'A8': '0'}

    output = ""
    for i in range(0, len(word), 2):
        output += HexToWord.get(word[i] + word[i+1])
    return output


def createOutputString(matrix):
    output = ""
    for i in range(4):
        for j in range(4):
            output += matrix[j][i]
    return output


def xor(a, b):
    a = hexadecimalToBinary(a)
    b = hexadecimalToBinary(b)
    output = ""
    for i in range(len(a)):
        output += str(int(a[i]) ^ int(b[i]))
    return BinaryToHexadecimal(output)


def multiplyHex(a, b):
    return hex(int(a, 16) * int(b, 16))[2:].upper()


def s_Box(matrix):

    s_box = [['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
             ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0',
                 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
             ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC',
                 '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'],
             ['04', 'C7', '23', 'C3', '18', '96', '05', '9A',
              '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'],
             ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0',
              '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'],
             ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B',
              '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'],
             ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85',
              '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'],
             ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5',
              'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
             ['CD', '0C', '13', 'EC', '5F', '97', '44', '17',
              'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'],
             ['60', '81', '4F', 'DC', '22', '2A', '90', '88',
              '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'],
             ['E0', '32', '3A', '0A', '49', '06', '24', '5C',
              'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'],
             ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9',
              '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'],
             ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6',
              'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'],
             ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E',
              '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'],
             ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94',
              '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'],
             ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']]

    map = {'0': 0,
           '1': 1,
           '2': 2,
           '3': 3,
           '4': 4,
           '5': 5,
           '6': 6,
           '7': 7,
           '8': 8,
           '9': 9,
           'A': 10,
           'B': 11,
           'C': 12,
           'D': 13,
           'E': 14,
           'F': 15}
    try:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = s_box[map[matrix[i][j][0]]][map[matrix[i][j][1]]]
        return matrix
    except:
        for i in range(len(matrix)):
            matrix[i] = s_box[map[matrix[i][0]]][map[matrix[i][1]]]
        return matrix


def inv_s_box(matrix):
    inv_s_box = [['52', '09', '6A', 'D5', '30', '36', 'A5', '38', 'BF', '40', 'A3', '9E', '81', 'F3', 'D7', 'FB'],
                 ['7C', 'E3', '39', '82', '9B', '2F', 'FF', '87',
                     '34', '8E', '43', '44', 'C4', 'DE', 'E9', 'CB'],
                 ['54', '7B', '94', '32', 'A6', 'C2', '23', '3D',
                     'EE', '4C', '95', '0B', '42', 'FA', 'C3', '4E'],
                 ['08', '2E', 'A1', '66', '28', 'D9', '24', 'B2',
                  '76', '5B', 'A2', '49', '6D', '8B', 'D1', '25'],
                 ['72', 'F8', 'F6', '64', '86', '68', '98', '16',
                  'D4', 'A4', '5C', 'CC', '5D', '65', 'B6', '92'],
                 ['6C', '70', '48', '50', 'FD', 'ED', 'B9', 'DA',
                  '5E', '15', '46', '57', 'A7', '8D', '9D', '84'],
                 ['90', 'D8', 'AB', '00', '8C', 'BC', 'D3', '0A',
                  'F7', 'E4', '58', '05', 'B8', 'B3', '45', '06'],
                 ['D0', '2C', '1E', '8F', 'CA', '3F', '0F', '02',
                  'C1', 'AF', 'BD', '03', '01', '13', '8A', '6B'],
                 ['3A', '91', '11', '41', '4F', '67', 'DC', 'EA',
                  '97', 'F2', 'CF', 'CE', 'F0', 'B4', 'E6', '73'],
                 ['96', 'AC', '74', '22', 'E7', 'AD', '35', '85',
                  'E2', 'F9', '37', 'E8', '1C', '75', 'DF', '6E'],
                 ['47', 'F1', '1A', '71', '1D', '29', 'C5', '89',
                  '6F', 'B7', '62', '0E', 'AA', '18', 'BE', '1B'],
                 ['FC', '56', '3E', '4B', 'C6', 'D2', '79', '20',
                  '9A', 'DB', 'C0', 'FE', '78', 'CD', '5A', 'F4'],
                 ['1F', 'DD', 'A8', '33', '88', '07', 'C7', '31',
                  'B1', '12', '10', '59', '27', '80', 'EC', '5F'],
                 ['60', '51', '7F', 'A9', '19', 'B5', '4A', '0D',
                  '2D', 'E5', '7A', '9F', '93', 'C9', '9C', 'EF'],
                 ['A0', 'E0', '3B', '4D', 'AE', '2A', 'F5', 'B0',
                  'C8', 'EB', 'BB', '3C', '83', '53', '99', '61'],
                 ['17', '2B', '04', '7E', 'BA', '77', 'D6', '26', 'E1', '69', '14', '63', '55', '21', '0C', '7D']]

    map = {'0': 0,
           '1': 1,
           '2': 2,
           '3': 3,
           '4': 4,
           '5': 5,
           '6': 6,
           '7': 7,
           '8': 8,
           '9': 9,
           'A': 10,
           'B': 11,
           'C': 12,
           'D': 13,
           'E': 14,
           'F': 15}

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = inv_s_box[map[matrix[i][j][0]]
                                     ][map[matrix[i][j][1]]]
    return matrix


def galois_mult(a, b):
    a = int(a, 16)
    b = int(b, 16)
    p = 0
    hi_bit_set = 0
    for i in range(8):
        if b & 1 == 1:
            p ^= a
        hi_bit_set = a & 128
        a <<= 1
        if hi_bit_set == 128:
            a ^= 27
        b >>= 1
    if len(hex(p % 256)[2:]) == 1:
        return "0" + hex(p % 256)[2:]
    else:
        return hex(p % 256)[2:]


def shiftRows(matrix):
    output = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][(j+i) % len(matrix[i])])
        output.append(row)
    return output


def inv_shiftRows(matrix):
    output = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[i])):
            row.append(matrix[i][(j-i) % len(matrix[i])])
        output.append(row)
    return output


def mixColumns(matrix):
    static = [['02', '03', '01', '01'],
              ['01', '02', '03', '01'],
              ['01', '01', '02', '03'],
              ['03', '01', '01', '02']]
    output = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    for i in range(4):
        for j in range(4):
            r = []
            for k in range(4):
                r.append(galois_mult(static[i][k], matrix[k][j]))
            output[i][j] = xor(xor(xor(r[0], r[1]), r[2]), r[3])
    return output


def inv_mixColumns(matrix):
    static = [['0E', '0B', '0D', '09'],
              ['09', '0E', '0B', '0D'],
              ['0D', '09', '0E', '0B'],
              ['0B', '0D', '09', '0E']]
    output = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]

    for i in range(4):
        for j in range(4):
            r = []
            for k in range(4):
                r.append(galois_mult(static[i][k], matrix[k][j]))
            output[i][j] = xor(xor(xor(r[0], r[1]), r[2]), r[3])
    return output


def roundFunction(word, round):
    roundTable = [['01', '00', '00', '00'],
                  ['02', '00', '00', '00'],
                  ['04', '00', '00', '00'],
                  ['08', '00', '00', '00'],
                  ['10', '00', '00', '00'],
                  ['20', '00', '00', '00'],
                  ['40', '00', '00', '00'],
                  ['80', '00', '00', '00'],
                  ['1B', '00', '00', '00'],
                  ['36', '00', '00', '00']]
    word = s_Box([word[1], word[2], word[3], word[0]])
    for i in range(4):
        word[i] = xor(word[i], roundTable[round - 1][i])
    return word


def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    output = []
    for j in range(columns):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        output.append(row)

    return output


def keyExpansion(key):
    words = []
    keys = []
    output = []
    for i in range(4):
        l = []
        for j in range(4):
            l.append(key[0:2])
            key = key[2:]
        words.append(l)
    for i in range(40):
        l = []
        if not len(words) % 4:
            l1 = roundFunction(words[-1], int(len(words)/4))
            for j in range(4):
                l.append(xor(words[-4][j], l1[j]))
        else:
            for j in range(4):
                l.append(xor(words[-4][j], words[-1][j]))
        words.append(l)
    for i in range(11):
        keys.append(words[0:4])
        words = words[4:]
    for i in range(len(keys)):
        output.append(transpose(keys[i]))
    return output


def reverse(matrix):
    output = []
    for i in reversed(range(len(matrix))):
        output.append(matrix[i])
    return output


def addRoundKey(matrix, key):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = xor(matrix[i][j], key[i][j])
    return matrix


def createKey(word):
    if len(word) % 16:
        word = word + (16 - len(word) % 16) * bogusElement(word)
    output = ""
    for i in word:
        output += ''.join(format(ord(i), '08b'))
    return BinaryToHexadecimal(output)


def encryption(plaintext, key):
    plaintext = stringToHex(plaintext)
    print(1, plaintext)
    plaintexts = createInputMatrix(plaintext)
    print(2, plaintext)
    keys = keyExpansion(createKey(key))
    ciphertext = ""
    for plaintext in plaintexts:
        state = plaintext
        state = addRoundKey(state, keys[0])
        for i in range(1, 10):
            state = s_Box(state)
            state = shiftRows(state)
            state = mixColumns(state)
            state = addRoundKey(state, keys[i])
        state = s_Box(state)
        state = shiftRows(state)
        state = addRoundKey(state, keys[-1])
        ciphertext += createOutputString(state)
    return ciphertext


def decryption(ciphertext, key):
    ciphertexts = createInputMatrix(ciphertext)
    keys = keyExpansion(createKey(key))
    plaintext = ""
    for ciphertext in ciphertexts:
        state = ciphertext
        state = addRoundKey(state, keys[-1])
        state = inv_shiftRows(state)
        state = inv_s_box(state)
        for i in reversed(range(1, 10)):
            state = addRoundKey(state, keys[i])
            state = inv_mixColumns(state)
            state = inv_shiftRows(state)
            state = inv_s_box(state)
        state = addRoundKey(state, keys[0])
        plaintext += createOutputString(state)
    plaintext = HexToString(plaintext)
    return plaintext


# plaintext = input("Enter the text you want to Encrypt: ")
# plaintext = """b'/ 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"""
password = '0x8dbe50f423ef43cde40a9fe85a3319bb5542fda61af4f726efbfb7230dae49a70'
path = r'C:/Users/Shreyansh Jain/Downloads/ILTQq (1).png'
fin = open(path, 'rb')
image = fin.read()
fin.close()
image = base64.b64encode(image)
image = str(image.decode('utf-8'))
print(99, len(image))

p = ''
pas = ''
# image = """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"""
# image = list(image)
# image = str(image)
# print(image)
print(set(image))

d1 = set(image)
dict1 = {'A': 'F0', 'B': 'F1', 'C': 'F2', 'D': 'F3', 'E': 'F4', 'F': 'F5', 'G': 'F6',
         'H': 'F7', 'I': 'F8', 'J': 'F9', 'K': 'FA', 'L': 'FB', 'M': 'FC', 'N': 'FD',
         'O': 'FE', 'P': 'FF', 'Q': 'E0', 'R': 'E1', 'S': 'E2', 'T': 'E3', 'U': 'E4',
         'V': 'E5', 'W': 'E6', 'X': 'E7', 'Y': 'E8', 'Z': 'E9', 'a': 'EA', 'b': 'EB',
         'c': 'EC', 'd': 'ED', 'e': 'EE', 'f': 'EF', 'g': 'D0', 'h': 'D1', 'i': 'D2',
         'j': 'D3', 'k': 'D4', 'l': 'D5', 'm': 'D6', 'n': 'D7', 'o': 'D8', 'p': 'D9',
         'q': 'DA', 'r': 'DB', 's': 'DC', 't': 'DD', 'u': 'DE', 'v': 'DF', 'w': 'C0',
         'x': 'C1', 'y': 'C2', 'z': 'C3', '.': 'C4', ',': 'C5', '!': 'C6', '@': 'C7',
         '#': 'C8', '$': 'C9', '%': 'CA', '^': 'CB', '&': 'CC', '*': 'CD', '(': 'CE',
         ')': 'CF', '-': 'B0', '_': 'B1', '+': 'B2', '=': 'B3', '}': 'B4', '{': 'B5',
         '[': 'B6', ']': 'B7', ';': 'B8', ':': 'B9', "'": 'BA', '"': 'BB', '?': 'BC',
         '/': 'BD', ' ': '00', '1': 'BF', '2': 'A0', '3': 'A1', '4': 'A2', '5': 'A3',
         '6': 'A4', '7': 'A5', '8': 'A6', '9': 'A7', '0': 'A8'}
# d2 = set(dict1.keys())
# # for i in dict1:
# #     d2.add(i.keys())
# print(d2)
# d3 = list(d1)
# d3.sort()
# d4 = list(d2)
# d4.sort()
# print(d1.union(d2))
# d5 = d1.union(d2)
# print(len(list(d1)))
# print(len(list(d2)))
# print(len(list(d5)))
# for i in image:
#     print(ord(i))
# for i in range(min(len(d3), len(d4))):
#     print(d3[i], d4[i], d3[i]==d4[i])
# print((d2.union(d1)).intersection(d2))
# for i in image:
#     p += str(i)
# print(29, len(p))
# pas = ""
# for i in password:
#     pas += str(i)
# encryptedImage = encryption(p, pas)
# print(p)
# print(encryption("""YWkwMXhmQ3pLZUpJaDlZRDQzN2RLVVdsV0F0YWw2QTg0UlNIeGxvQlk3UEozbFY5Qys4Y1FpRlNrUjY3dVJsaEQwRkx5eTBJejBuVXNkdm53Q0Y3M21YK3cyUjI5UENzTG5yNEsyNUNyMHdQUkZyS2htNHA5WEVaMFNVNTZRb0NtM0Iya2YyajRLZWMyK1lOdWZWNGJsZmpMV3ZzR0l6eWVQaS9EUXdEVFdlWWFmSkVkTkJScTdEdGs1dXFkSXZhVys3OEJYL1VSdGVYdStTK1lFdWhLUnhoVnZUWFRRamdLb1VncmZiOE5qOFpoSmE4UlphVDhOY09idGtjdUNtdnBCNkllRForMTRxTHR1OEdJVjNnbURwM1k5SXAvRzNaNGJLektZTlBDY256Z2o3NDdiSE1hYnpaWUIxZkZQaDNuY3NyUDRta2ZHRDdJdnh2SE84eHN5Y0RKQWZhUlNEM01TdGZiSU41S2FGOWJHc2prcldVVFByZVFDWkE1M2pKMitZUDNDQ2UvcS84N3NaWkxoYXB1RmNlKzhHelFqaFhKZTREMmZoaVJET1NwOVRDYkYzcDhvNWlDcG5CUldrSk5PK0tJVktCS044NkZHQWsvejQ3Um1sVTVMRGVEekRDR21NWjJzYWdpSGxScThNM1UvL3FqRks3OFBidm5Fc3pibHpldExtT1FhYXg5OWFlSHVJd3BJakJ3eTVpbURXUC9HdUFQWExSYlVHay9uOFF6QjJUdGpDYVI4TGxOdmh6WWl5eVZ6WXhZV0hLMHJtT2JWcEdCUG41dDhkV3hQdVdmS2REdGRkVGkxcVphM2NCRkVBSVdOa0trTnU0bWd2OTBlbjhtcCtEbXB5RzZvYXFEYUNLR2wvamlYaVYzZy9NSTNmMy9tSElTWUsvbVFYU0FKZ1F5SWxySlJUVkhUM0RnRmtRM3pqeWZwSEx4Yit1RkxCRlphQzZWd2ZmRDhWc1BGT3dHZ2ZCdDd5VTl4Nkw3ZFc3c2pjTmVscGVUdWhzSGxzYTAraXRMbDBNZzVMMHo1RmJQd1Z5V1FxdGh4TEpaaFhCUWxaNWhlSHV2UW5DdWZINXlGT2ZUSUxQbG5FdmJOR1A2YStvRzlUeWhyK3BVODhqYUpxcTNmc1ZEYmxiSm9UL2x4Zk1DQXB2Z3ZUN2tlaTNTZVhVWXVwdUtueXNtNmd2TGRXak1ySkFRWTRIMTBVaXFMRmpNZEVtaFY2dHVjWlQzUUE1UHBENktDVHNJbDlhUmtzc2h2VzJnOTdSbDZZbnFHa2VvbFdNRldST3NsNm9uMGNucjNSVWFWbjUvUVpLaS96TVdMaEIxL3huYS9FL2RQeG9FTUhvd3dKbXl0S1lKbUJoS0RTUSs3UHpHU1Urd1o4Vjk2emhLWFRjNHZhTElTaUxQVEluL01Sei91MUhJbXdsMGhlTm56SlA1SnZxaElVbVFsY1NOdllIMGh0THdscW9sZnNVSkpxVjhLaU5wcEp4K0Z1bS9sSCtYVW5JMTJWK0pBS0RVc0p0c0tnYWVYemdYRW1mZjVuMFN1VTA5YTdqU3BxcFp5dkpYc2dDVysrSmVpUUZlSHRvMzh5UGJvU0VoaFg2QjFUT0JueWh3bFlzNFFKR1RrTHExZWZ6WWRCbG5JcDFmcHUrK2F3K2o0cWRUUFBJNnIydTNwaDFrUGo1N3RWMkRxYmN2UU90bFFycHJRb3BJV0h2U2x1dHNaM0RIcFdqWTJjcEdnZW8wZW1RMWp1RGx4alN4Z2d4UmJCc0FqTWxKRGg2bERpMXM0YmFJeFovRFJIUVVBYitCSUtEcjU0VVVkQy9rdVhXOVRXaE5pSGFLMzJhcEM2bEpWVTNkeGJIekdqWkk1b3NrSkxzVlp4U3lTT1A3SU9rNXlJVjk5aWI2VG83bGxpME5tbUtpOFVpamRBc050QVU1aGlDL3c5TU1aMEx5TWM3Qk5BRUVCeWpDN05MWVdMcDFDM1pvdE52V28zSUNvS0x2bXR1ellXRlNSYnd1Nm1WeS9CRjIvUHIzZVY5c2ZKSi95aC9XaFBjQ2Rib21nTmIrZW9YbkFjd09sa0ZvaFpYMTVDclUrWksxaFR1K3RQMGZUMWJXTjVERmtJbTZEUGVrSFZ4Skc5TStlYnZteE4wZWxYUXBqWmViUXJPVzU3c1UvRUdlaDlwZzhNdDdla0VvZmt5eWtYL1R6V3VlRHZ2d3J3ZkIvOVJQSGFwT3hOYmxDM1NXQnBjeEwvS0VoTTFNNS9TZU9hb3Y4UHpHa1pJU25TcW95a3ZpS2VIM09GWGhTYVdJR1FRZFJ4bUZrM0VreWhYQ1hONW9VNUdjZ2JSbVhwdXcrd2hOTzE5c1BSTXRXNEtNSG1UVDg3MDFMcmdkdE1aUWVDWlE2cHk2U1BYQ09mZGNNUzBpNklNTjV5NlFMVDRVWk44a0dmMlo2VTZtSUZ4aDVoUFkzeVVLeS80Q3pmb0hjNEJ0cDRaYTUwL0hPWG8xZlZLUm1PREtvNDBXU2dsYk0rNWRTV2lCTE1zeG16a0xqVWJpMEIyR05BUjFuS1UzUFBGbytEMXQ0ZjhDT0lWcUg4WC8xSURodmZ1MW1hMzRYb3NuRzAxeWd5R1VNZzI2T0tkY3dLOGNFbWNyNUlKZzMrd29iREt3b1dFaTFNQW9TdGF5VWtXdk9ENTFreDdVYVlIOW5SYU9waEt4LzBQKy9YQlN5RWtNMitRaHVxOUNJR0phK3F4YmpSZlZBR21HcURFcmdNVG9xajc2SzJ1b1p2UDQ0blJqd2hsVTV2dzFsWW5qWnB6VFBWbC9BWFdkM0U5YVhzOU9XcTNsSjFXb05BV0hQRVROWElSNWk3UzZFMTJBT0ZseTF6Q1hhWWZ6OEQ4QW5Cd05mcG1Jc0tCR0JMOGZ5TWRhM1ZleVRySjIxQjRoaFlobytINExST01ROW5FcWNnNjIyVHVhMUtBUTRtVEJrQ1BGTGl2SUJlZEVydHBXZDJvZWhiRVBMY1htdS80Z2JYN3JzSndtSWk5V1NRUkU1cUlnTTlpU2I5UmZUSDZvNjdXRzhkNDhFa1pzakpZQlNGQ3dCbmd2OHBySW1WdWtDTy9jLzI3SmdBVzJMWGd4MVNCNlV3Yi8yR1A1eFVnZjUycHl1UzVPSHZYSHE2QXNnMUNHS0h1bEgyQ3pRWWkzZ2ZvUUY5Y1p3RHEwc2hFZ3gxQjlQRmVBV0FWQjl1REc1TFJjeDlEaWNBeU45dXBUVG9GODBNMk15R2Z3QXRwSXlhd3RZNmJLbUh1L3NZaktLSnVKN0dzQWVVMUc2ZXB5N1NaZUd3eVNNdGVCYURUb001Q3drb3ZIRmJBNHJaeFFDSGhBY1UwaW1CWmt2M0tEWndwRUpUZG5BZTFSOGtLN2k5WWp0ZkJITUZyRzFrS0ZJSDF6M1ZIdzZtSDN4UTZmczl1alAyaVU2T1JPb3h2aCtBdDVDZUlMRDRZV1RrcDBFbFJUZEFvL2xML1diNWp2WWRjT3VwVjUvOWhHNUtkZVJCV2xTbi91QzYvd2FDTzBzNThwT3FTUzNOTXhHakxpa2lQVXFWNFNxeUtPL2hZVi9LYi9FbG9ZOHZqQlFxVnJ2NDhCbmxIOFR1ZFVBejlGcjBOc01Samh0MnAxT25DWUwxcjlpb3UwZ0tBWnQxdHJrMUMyeUhwdVJ5N0s5UVJYVEZscXY4VXpPZ3N2dG9XR1FDdm42cTBTOWEycjZwTE1yZWRuN3dQWkpqdzkrbUJZampNWDR3b3g5MTg5dVY3YjdKWWRHODZwTlFwSkM5MGNMc0Q0SjU0OG5nTkVud2VxTjhub0w5dXcybk40aGQvRW4vYmdSd2N1SStvSm1qQVRoRjgzdUVaQ0pCdThEcXpFMm9UMS9ZSTBCT2ljenpHek11NE1ZMHpJMGVVTFQ3dzBhaG5pVUNZSG9rbXYvdnJValVGSjBpY0dxeW9GUldwN1RiSU42V1pWQytka3VrTi9PRHNSc1B5aHJFWmNWUW1zMXlyVERoeDdOR20ySTVFNTlSVjFVNmhGOEtPZVM1SDZIMUszbzlvZ3M3TjU1aHdyWk9TYkgwN0RFdFBRbGNXdFdUdUZ2bkE5cllpck9qbWlrTCtBZjkxLy96M2RtRWYxMVFNR3ZqWDE3RzViRVJ5WXZqRWVQdTY5NkRpcUdFSDdzUENaU0dUdmRYZlc3RWJ1WTgzQlRSZlV3ZGNtTHQxZkNiNXBqQnAxVjVmaDc3NnNZVDdZaTJNT0srRlZNa01aVjJVNi9BZURsVm9maXJGQ0c4aTZ0OFJJTE1ycG9qbURzTlF2K1V0Rjc0dVk0YzhnOFpLN203VFJaa2tIVUVLSDZQa3pzdnlkODd0ajZRRkhPNVN0dXFGUjBtOFlMQWx6WXJVUTNBbm9kaXVsQ3B1c3I1d3lUcDdNb0JpU3NpMkJvWC9JdXJLZG5GQ1p1WEozRUNRNENnKy91SEZhVVhLWE1yUllqMzNweHdiU1FNMG9LdW9Ha00wd0NDSzRLV2U2bk4xNVI5bEJsdUxDTmJIU0VncWR6NzR2K09MVjh2Z0xYRzl3TW5UcnhUM3NrYWE3N1RHQlpQVlNqQm52WlAxYy94dkhTR3IxTzJpOHhINWpyZ21DZ0paVU1Nck40NENMcTMzWVdGSlo0YU9EOHVkS0kvUldoc0orSG9QempVdlVoWXduditSU3FUUnJQNzJ5TURoUU5TM1Jkd2NvNmJyOC9xSGtPcWVIamRLcmV3L212RThKQ3lmQ2Nqb2Z5alg5ZXZ5Zk16S1dpUGZ2SDFtY1FIb0J1aVRGZ2lDa0p4ZWJvdHlGanhidHIxOWs1MDRWWm9paUJ6bmZIQXB5MXcyRmR4ZHExZlRTUk5Ba1VYeng2WHVNL09QWUJWNUF4dTM0eisyeGl0dnVQczJNSFlJSVhFb21YS0c5VGRUTmRBRDUrL08yVUtoTnZCKy9wb0VHZURLczgvMGxYbEVGbHE4Sm5PRldJSGRUQm54T3pBSkh2UlJNY3R1eEJPV0xDOEZnM0Rkc1RVNjVDVjE5N0VZUklzQ2pSSjZNRkYrclR6bTNDRUxGRGJ2UnFpRFFFc0xnamNXNHo3cUpiLzlQa0RSdElEbElJby8xT2lBdUhJa3VVeW90T1BvWG5ha3FoRUFoRFVMTG94b2N0VWtocTFORWREMlE5VmtZSjVKQS9rMkZQRitFWXBBRWU0TjIyTjgxLy83ZnZJUWNTbXoxMndNek96QXBGeFlpdDVldm5uZVYwOXpRY1B2Y2NxUVlYcXBJYXlQTWxmZEJvNEthaUV1MFhFWlMwTG9RbERsOVo3U1h5QzRsdit5RUtUcEEyZjNLVkNzRkdPMGZSTUc3Sjhob2czc2VuZTRhM05pTTZ2aThldU1kdlM5VEk4VnJiemtTL1B0Z2FwdkhyZ2ExbEdtdUpGOXprR1d4ZVBnVnpPb0FvcmRQNXZVNkNkR0VZU256Tnk0eHozeVZDWitvbm9zcDVNUk40b2pvT0NJTTRuaVV5ZHFvM3lWL3ZtTnV2R0w0aUdITnR4dXRhNi9Ka1YzM2dvOXRzcExsclgrZUhOL29mL3FoeW4rdVBXQTBKNTZsUHFjVnJEWHE0Q0wwRDZHMmM5YXVuMS8yWVVFa0xBOHFhOElXcU03MS9TelVFOU9Tc2xiL2hwU1FkTjFMOHpxdUpneHltdmxCMzNuUDlFdTgwN2JhNDBZS0lPbnZTZ01xVTRPQVgxdXNTUVV2M0dIVm9lSUdnM1VjdS80bWkzaWlPcmpwMktLazR2NEc4VWlPQWtrMS9rbnRBVW5YOXFKZFVtS0pINWZ2OUpJcThpQUxKUGhrV0Vyd0YxOXI3S2RodG9lWU9YODQ2VUFsZlp1d2pyUVZsNk1pa2o5cTQwZElmS1FJbGtkcm5NZnpkaTVDdW5adFNxNmtBNkkxNmY4dmV5c0RFdnZodHNnY2hCeFNqajRiT3lxdHZablB1ZWVHS0lyTEJZWUJpcDRSdWJsU0RHUlJCRk91aWplNFozUEZrOVdnTTMzSzRNeWNDbkZ4ZmVqeFFla0RZcElkdmo0YlF5MERJbUt1OVRiVUhueHpsdTh3ekViVWRQVlFqN1NJWnN6R05oVnJyRm1JWkt4SEtOR21vMld5WWYxajNJdU4wYlp4dlh3OXg0cWhma0IwcG1XQmtWcldpbjJ4Zm95cjBxSVdMZ052MHQ2djNQOHlTUzh0QitRcXRSemZEMGMrcDRpcUNiZHF4VEFLRTFSUGdRb1huRnVFK3lxOWRCbzM1YTFVbktONzBxMUZVUlA3SjZIbjJEazZLbkk5RWxvMGZXNEdoaG83eUVYaTd6eExnOHRMd0xySTFZRkpnV3ZSNUdLcHYweUtEdGIrdUwxeU9OdXpBekdmRXV6YW45ekdJZlZKTU9KbnNocXNJc3UwU1BzYjdpaEtQUGpnRFl3SHhTN2ZXMzBCb0J1UlBXOXRHOW9KZlZ5VkUzcEZWSXBxSWhYVzZRU3YwN1RhckoxbS9iWXN1YSt3L2Z5MWZ2cXFFeHo2QnVRcTZyUTg4MS95aVlicnBsNmJ4ODQzMGdLTXdQdWZrbVpXbkhiZk5pZ253M000SVcvT25xUXl3M1RSVHdlUEVza25jK3pSaE5VNTFmNVZvcCtQRDlYaUhhNWhYQXk1dDJiVkRsREFoMW84bHh1UkJBL3hNVFhzdWg3eHNoT2c5dVozMHdZbnY0cm12Si8yUklNUXNNZEdmRy9iUGV2M1pQa0NaT3l2N01CbWt6Wjh5czJqNi9RTVRLc0dqV3FaTWtJSG9hNzFYT2ZNTnpzTEh4OGtoQWZlY1VTa09rR1hvNWNKNVZOSkxmTG13bDZlelZrTGIvY0NwWHhVdFJYKyt2bE5YcUlmSlBIWkVHNHJSV00wUkxLeUdCdDBXWUdldmJlclBrOEMyc242SGRlbG94U0RUSHBycGErRVNpdG1kem5lNHlvQWhwWTJsa3hTWHVId0lUNlJ3QWdVSU1McjVnYjlzdUlnK21YdGN0OG4va3dhL1JxMGhTV3NNMUVNWWl6ZlFrc1ljUFlPazlQb3NLRmlBYkZoNkE2Y3YwUlJQU3pHOXhOL2s4aXU5RzByQ1p4dmxDdDltblEvclMveldQd3VwM3ZRUlJiY3BaU1B3N1JVTm9jaFZiYXVpcThMQXNqNk4vbXZjSjFkWGoyTXQrUjMrc3VodXI3T1B5dE1FRHkzakZIV2F0c2ppbjJ1TU9DaFcwZVgycFRFdjR0L2VzV1VGVWFHdHlpVEtxbS9Nb0t2NER6dHdLRHJtSHAzK09WZWRZaCtTek0zZ0NhamNiYXg2Y2tlRWRpOXAzVTU4Qmc0NVN0TFJPV2ZIbEtLNmsySHdKbjY4c0lHUGhrOTJtRS90L2Z1QVZYMjFlUXF3SVh5eVBKOWVBTG5KMVo4eTFMZS91NHI4ZEN4clVtWlRFOU02SE8zYy9laHRjRlFkc3RmU20vU2dVMnNsOGkvYzlnTXR6QUxRRm1RVkhPbmkwVkh2VHphU3ExQ1dWYUdoTlJFek9QdW9YRkdzUHQ1aHBoV3AvY2tER25iM0VLWVpIZW9DcEd0em1jZnFWR3grR2hyNDREMXgvRERYTWIvaUhiUG5Zbng2alpFUVBsQVhwUjAwTzU3Tkh1U25EZ3lTdzBIK0xxSk0rZDNEaWJ3MjgzOFVzSlNnMWtGWUhlVXJIcERrS0h3SjJ2T0s1U1djd0haRWhKdkVVMXFYQ3RqWm54eG5KMlo0UFZuQSswVDYwZEc0bUFBTHZyenJnOW0raGcrNm45RnMrb0VobE5rNGZIeE1VU1pSdFljN1FtYnBLNUo3b2VzUTZBcmJ4b09MaW5TclVUMFBiRWl1QmtFRWxKaVhrNFRFck9lUklOakhSOHp5NGpQaFF0bFBEWU1UaDNaUWZXSjlLUGRhN2MvQzhLYU1zTkVjTEhhOVhwVVJsV1hHRDU2RTB4R0ZlZGlhOG4wditROEVZY2l5VEpoSVMzQzgyT0NQbFpHbzlmMFhYUWVaNis5Z1NDYU1HajJGYkN0ekxZWmZKekJXSmozaXNMUkV2UXd0aXhoWlp3NHNYcnlrWWFmcUNaRi9pekFrZysvNmxtWGZ0V0JzVjR6cnd5RCtZQ2s3ZU9JZ05rYmxGNlQ1UlFlbkFWd2xTTi9YZ1liZ2U0cUtnQWU5dE9TTysyaytxNGVaaU9GbDBoUU5QbHdnblpZdU5vQk9TaHllMDM2VmptU1cyQk1Zb2l6Q3ZwMHNyZ1V6YzNXaFByT0NId2hmRFl4OHBFeEp0RlVlekx5dlZWZTE5ZW1ZSkRuR0ZndU5XMkVjL3pXd0MvTFFDNnRjd2lxRldOS2pKamJEMlRqZlIxdW1TY3dWZENvZWZKVkcrc0NUWlhDem40MjVWdnVUT2lGSnFOQU8wK0FhR2pQTFUza0xTN1ZuMWpMVXg3OVBFeVNjNVl0TjhuOVloL0ZadExJTC9XcktUWkM1dVJ0WE10ZHZGWTkwQk9tTndtQmViSXZEMzRvZDY5M1NWek9uUXdKQjBpbk1venBoRUhGaWJ4eDFuOFJGeHp2anNhaHFuckw1ZzBSeEMwMngybzZ6Y05PL2pjempnMVRPNVZQUWs5RHFuV3NFNk55cXJTUWdUUzByblR1SnU2eURURWoxdFJESTNteHRGN2E3azNoTFRieHlodVZ0WTlmaWx3TUl1VXhQY1pvZFBGQ3JaSkJOZDBqY3Q0Nmg0N3E5KzFLN0JOVUZlRk9kY0VlZkFTRjFtNUtmeTNLTWZuYUNxVUM3cllqb2QzalRiNXQvV01tQzJGNEZKTWxhU3YxZzhmeXFlRUVncnQ5TmVPTzV6alp5Qjc5c21aMmM2Ym1kb1pjUHNKZUJaWXp6dldPUkNDdUpxZzNVOVRKYUNaOHlmeG1sSGVKS1VLL0hBR0M1dXR2aElrWVJHYlFvd2hxWDZHcWZrVGhvYUltVHJ1dVhDT2IxZXkydlht""", pas))
# print(encryptedImage)
# print(stringToHex(image))
# print(encryption(p, pas))
# # key = input("Enter the key: ")
# key = """0x8dbe50f423ef43cde40a9fe85a3319bb5542fda61af4f726efbfb7230dae49a70"""
# print(f"The encrypted text is: {encryption(plaintext,key)}")
# encrypted_text = input("Enter the encrypted text: ")
# decryption_key = input("Enter the decryption key: ")
# print(f"The decrypted text is: {decryption(encrypted_text,decryption_key)}")

# path = r'C:\Users\Shreyansh Jain\Downloads\wp4676584-4k-pc-wallpapers.jpg'
# fin = open(path, 'rb')
# image = fin.read()
# fin.close()
# image = base64.b64encode(image)
# image = str(image)
# # print(image)
# encryptedImage = encryption(image, password)
# print(3, createInputMatrix(stringToHex(image)))
# print(len(image))
