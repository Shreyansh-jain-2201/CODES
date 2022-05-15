# Shruti AES

def reverse(state):
    op = []
    for i in reversed(range(len(state))):
        op.append(state[i])
    return op


def input_state(pt):
    hex_text = ""
    op = []

    if len(pt) % 32:
        pt += (32 - len(pt) % 16)*filler_letter(pt)
    pts = makeGroups(32, pt)
    for pt in pts:
        pt_state = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]
        hex_text = ""
        for i in pt:
            hex_text += i
        for i in range(4):
            for j in range(4):
                pt_state[j][i] = hex_text[0:2]
                hex_text = hex_text[2:]
        op.append(pt_state)
    return op


def makeGroups(bits, num):
    op = []
    groups = int(len(num)/bits)
    for j in range(groups):
        op.append(num[0:bits])
        num = num[bits:]
    return op


def filler_letter(pt):
    letters = list("0123456789ABCDEF")
    pt = list(pt.upper())
    if not "0" in pt:
        return "0"
    else:
        for i in reversed(letters):
            if not i in pt:
                return i
    return "0"


def bin_to_str(num):
    op = ""
    for i in range(0, len(num), 7):
        op = op + chr(int(num[i:i + 7], 2))
    return op


def bin_to_hex(num):
    num = makeGroups(4, num)
    ht = {"0000": '0', "0001": '1', "0010": '2', "0011": '3', "0100": '4', "0101": '5', "0110": '6', "0111": '7',
          "1000": '8', "1001": '9', "1010": 'A', "1011": 'B', "1100": 'C', "1101": 'D', "1110": 'E', "1111": 'F'}
    op = ""
    for i in num:
        op += ht[i]
    return op


def hex_to_bin(word):
    word = word.upper()
    ht = {'0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100", '5': "0101", '6': "0110", '7': "0111",
          '8': "1000", '9': "1001", 'A': "1010", 'B': "1011", 'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"}

    op = ""
    for i in word:
        op += ht[i]
    return op


def create_output(state):
    op = ""
    for i in range(4):
        for j in range(4):
            op += state[j][i]
    return op


def xor(a, b):
    a = hex_to_bin(a)
    b = hex_to_bin(b)
    op = ""
    for i in range(len(a)):
        op += str(int(a[i]) ^ int(b[i]))
    return bin_to_hex(op)


def subBytes(state):

    subBytes = [['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
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

    dict1 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    try:
        for i in range(len(state)):
            for j in range(len(state[i])):
                state[i][j] = subBytes[dict1[state[i][j][0]]
                                       ][dict1[state[i][j][1]]]
        return state
    except:
        for i in range(len(state)):
            state[i] = subBytes[dict1[state[i][0]]][dict1[state[i][1]]]
        return state


def inv_subBytes(state):
    inv_subBytes = [['52', '09', '6A', 'D5', '30', '36', 'A5', '38', 'BF', '40', 'A3', '9E', '81', 'F3', 'D7', 'FB'],
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

    dict1 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
             '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    for i in range(len(state)):
        for j in range(len(state[i])):
            state[i][j] = inv_subBytes[dict1[state[i][j][0]]
                                       ][dict1[state[i][j][1]]]
    return state


def GF(a, b):
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


def shift_rows(state):
    op = []
    for i in range(len(state)):
        row = []
        for j in range(len(state[i])):
            row.append(state[i][(j+i) % len(state[i])])
        op.append(row)
    return op


def inv_shift_rows(state):
    op = []
    for i in range(len(state)):
        row = []
        for j in range(len(state[i])):
            row.append(state[i][(j-i) % len(state[i])])
        op.append(row)
    return op


def mix_columns(state):
    static = [['02', '03', '01', '01'],
              ['01', '02', '03', '01'],
              ['01', '01', '02', '03'],
              ['03', '01', '01', '02']]
    op = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

    for i in range(4):
        for j in range(4):
            r = []
            for k in range(4):
                r.append(GF(static[i][k], state[k][j]))
            op[i][j] = xor(xor(xor(r[0], r[1]), r[2]), r[3])
    return op


def inv_mix_columns(state):
    static = [['0E', '0B', '0D', '09'],
              ['09', '0E', '0B', '0D'],
              ['0D', '09', '0E', '0B'],
              ['0B', '0D', '09', '0E']]
    op = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

    for i in range(4):
        for j in range(4):
            r = []
            for k in range(4):
                r.append(GF(static[i][k], state[k][j]))
            op[i][j] = xor(xor(xor(r[0], r[1]), r[2]), r[3])
    return op


def round_func(word, round):
    round_table = [['01', '00', '00', '00'],
                   ['02', '00', '00', '00'],
                   ['04', '00', '00', '00'],
                   ['08', '00', '00', '00'],
                   ['10', '00', '00', '00'],
                   ['20', '00', '00', '00'],
                   ['40', '00', '00', '00'],
                   ['80', '00', '00', '00'],
                   ['1B', '00', '00', '00'],
                   ['36', '00', '00', '00']]
    word = subBytes([word[1], word[2], word[3], word[0]])
    for i in range(4):
        word[i] = xor(word[i], round_table[round - 1][i])
    return word


def transpose(state):
    rows = len(state)
    columns = len(state[0])
    op = []
    for j in range(columns):
        row = []
        for i in range(rows):
            row.append(state[i][j])
        op.append(row)

    return op


def key_expansion(key):
    words = []
    list_keys = []
    op = []
    for i in range(4):
        l = []
        for j in range(4):
            l.append(key[0:2])
            key = key[2:]
        words.append(l)
    for i in range(40):
        l = []
        if not len(words) % 4:
            l1 = round_func(words[-1], int(len(words)/4))
            for j in range(4):
                l.append(xor(words[-4][j], l1[j]))
        else:
            for j in range(4):
                l.append(xor(words[-4][j], words[-1][j]))
        words.append(l)
    for i in range(11):
        list_keys.append(words[0:4])
        words = words[4:]
    for i in range(len(list_keys)):
        op.append(transpose(list_keys[i]))
    return op


def add_round_keys(state, key):
    for i in range(len(state)):
        for j in range(len(state)):
            state[i][j] = xor(state[i][j], key[i][j])
    return state


def generate_key(word):
    if len(word) % 16:
        word = word + (16 - len(word) % 16) * filler_letter(word)
    op = ""
    for i in word:
        op += ''.join(format(ord(i), '08b'))
    return bin_to_hex(op)


def encryption(pt, key):
    pts = input_state(pt)
    list_keys = key_expansion(generate_key(key))
    ct = ""
    for pt in pts:
        state = pt
        state = add_round_keys(state, list_keys[0])
        for i in range(1, 10):
            state = subBytes(state)
            state = shift_rows(state)
            state = mix_columns(state)
            state = add_round_keys(state, list_keys[i])
        state = subBytes(state)
        state = shift_rows(state)
        state = add_round_keys(state, list_keys[-1])
        ct += create_output(state)
    return ct


def decryption(ct, key):
    cts = input_state(ct)
    list_keys = key_expansion(generate_key(key))
    pt = ""
    for ct in cts:
        state = ct
        state = add_round_keys(state, list_keys[-1])
        state = inv_shift_rows(state)
        state = inv_subBytes(state)
        for i in reversed(range(1, 10)):
            state = add_round_keys(state, list_keys[i])
            state = inv_mix_columns(state)
            state = inv_shift_rows(state)
            state = inv_subBytes(state)
        state = add_round_keys(state, list_keys[0])
        pt += create_output(state)
    return pt


pt = input("Enter the plaintext: ")
key = input("Enter the key: ")
print(f"The ciphertext is: {encryption(pt,key)}")
encrypted_text = input("Enter the ciphertext: ")
decryption_key = input("Enter the decryption key: ")
print(f"The decrypted text is: {decryption(encrypted_text,decryption_key)}")


f1 = open(r"C:\Users\Shruti Rout\.vscode\sample.txt", "r+")
pt = f1.read()
ct = encryption(pt, key)
f2 = open(r"C:\Users\Shruti Rout\.vscode\sample1.txt", "r+")
f2.write(ct)
text2 = f2.read()
print(text2)
f1.close()
f2.close()
