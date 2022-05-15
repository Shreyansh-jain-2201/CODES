def xor(a, b):
    output = ""
    for i in range(len(a)):
        output += str(int(a[i]) ^ int(b[i]))
    return output


def numToBinary(length, number):
    output = bin(number).replace("0b", "")
    return "0" * (length - len(output)) + output


def binaryToNum(number):
    return int(number, 2)


def scramblingFunction(x, K, i):
    return numToBinary(4, ((2*(i+1)*K)**binaryToNum(x)) % 15)


def encryption(plaintext, K):
    left = plaintext[0:4]
    right = plaintext[4:]
    temp = right
    ciphertext = ""
    for i in range(2):
        temp = right
        right = scramblingFunction(right, K, i)
        right = xor(right, left)
        left = temp
    ciphertext = left + right
    return ciphertext


print(encryption("00101000", 7))
