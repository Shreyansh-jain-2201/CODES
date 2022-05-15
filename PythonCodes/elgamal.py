import random


def numToText(num):
    numToAlp = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
                12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
                23: 'X', 24: 'Y', 25: 'Z', 26: 'a', 27: 'b', 28: 'c', 29: 'd', 30: 'e', 31: 'f', 32: 'g', 33: 'h',
                34: 'i', 35: 'j', 36: 'k', 37: 'l', 38: 'm', 39: 'n', 40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's',
                45: 't', 46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y', 51: 'z', 52: ' '}
    output = ""
    for i in num:
        output += numToAlp[i]
    return output


def textToNum(word):
    alpToNum = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,
                'X': 23, 'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 'f': 31, 'g': 32, 'h': 33,
                'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42, 'r': 43, 's': 44,
                't': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50, 'z': 51, ' ': 52}
    output = []
    for i in word:
        output.append(alpToNum[i])
    return output


def modularInverse(a, p):
    for i in range(p+1):
        if (i*a) % p == 1:
            return i


def checkPrime(num):
    counter = 1
    for i in range(2, num+1):
        if i**2 <= num+1:
            if num % i == 0:
                counter = 0
                break
            else:
                continue
        else:
            break

    if counter == 1:
        return True
    else:
        return False


def calculatePrimitiveRoot(num):
    for i in range(1, num):
        roots = set()
        for j in range(1, num):
            if (i**j) % num:
                roots.add((i**j) % num)
        if len(list(roots)) == num - 1:
            return i
    return -1


def calculatePublicKey(p, a):
    g = calculatePrimitiveRoot(p)
    h = (g**a) % p
    publicKey = [g, h, p]
    return publicKey


def strToList(cipherList):
    output = ""
    plainList = []
    for i in cipherList:
        if i == "[" or i == "]" or i == ",":
            continue
        else:
            output += str(i)
    output = output.split(' ')
    for i in range(0, len(output)-1, 2):
        plainList.append([int(output[i]), int(output[i+1])])
    return plainList


def encryption(plaintext, publicKey):
    plaintext = textToNum(plaintext)
    g, h, p = publicKey
    k = random.randint(1, p-2)
    ciphertext = []
    for m in plaintext:
        γ = (g**k) % p
        δ = (m * (h**k)) % p
        ciphertext.append([γ, δ])
    return ciphertext


def decryption(cipherText, publicKey, privateKey):
    cipherText = strToList(cipherText)
    a = privateKey
    g, h, p = publicKey
    plaintext = []
    for i in cipherText:
        γ, δ = i
        m = (((modularInverse(γ**a, p))) * (δ)) % p
        plaintext.append(m)
    plaintext = numToText(plaintext)
    return plaintext


if __name__ == '__main__':
    plaintext = input("Enter the text you want to encrypt: ")
    p = int(input("Enter a prime number p: "))
    while not checkPrime(p) or p < 53:
        if p < 53:
            print("The value of p is too small. Please enter a larger number")
        else:
            print(
                "The value you entered is not a prime number. Please enter a prime number.")
        p = int(input("Enter a prime number for p: "))

    a = int(input("Enter the private key: "))
    publicKey = calculatePublicKey(p, a)
    privateKey = a
    print(f"The Public key is : {publicKey[0], publicKey[1],publicKey[2]}")
    print(f"The Private key is : {a}")
    print(f"The Encrypted text is : {encryption(plaintext, publicKey)}")
    ciphertext = input("Enter the text you want to decrypt: ")
    p = int(input("Enter a prime number for p: "))
    while not checkPrime(p) or p < 53:
        if p < 53:
            print("The value of p is too small. Please enter a larger number")
        else:
            print(
                "The value you entered is not a prime number. Please enter a prime number.")
        p = int(input("Enter a prime number for p: "))

    print(f"The Public key is : {publicKey[0], publicKey[1],publicKey[2]}")
    print(f"The Private key is : {a}")
    print(
        f"The original plaintext is: {decryption(ciphertext,publicKey, privateKey)}")


# import random
# print(f"\n\n\n\n")


# def word_to_num(plain):
#     alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
#                  'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#                  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
#     pt = []
#     for i in plain:
#         for j in range(len(alphabets)):
#             if (alphabets[j] == i):
#                 pt.append(j)
#                 break
#     return pt


# def list_to_word(cipher):
#     alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
#                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
#                  'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#                  'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
#     s = ""
#     for i in cipher:
#         s = s+alphabets[i]
#     return s


# def prime_chk(n):
#     f = 0
#     for i in range(1, n):
#         if(n % i == 0):
#             f = f+1
#     if(f == 2 or n != 1):
#         return True
#     else:
#         return False


# def calc_g(n):
#     for i in range(1, n):
#         l = []
#         for j in range(1, n):
#             if ((i**j) % n):
#                 l.append((i**j) % n)
#         s = list(set(l))
#         if(len(s) == n-1):
#             return i


# def calc_public_key(g, a, p):
#     h = 0
#     h == (g**a) % p
#     print(f"Public key=({g},{h},{p})")
#     print(f"Private key= {a}")
#     return h


# def encryption(plaintext, publicKey):
#     plaintext = word_to_num(plaintext)
#     g, h, p = publicKey
#     k = random.randint(1, p-2)
#     ciphertext = []
#     for m in plaintext:
#         γ = (g**k) % p
#         δ = (m * (h**k)) % p
#         ciphertext.append([γ, δ])
#     return ciphertext


# def strToList(cipherList):
#     output = ""
#     plainList = []
#     for i in cipherList:
#         if i == "[" or i == "]" or i == ",":
#             continue
#         else:
#             output += str(i)
#     output = output.split(' ')
#     for i in range(0, len(output)-1, 2):
#         plainList.append([int(output[i]), int(output[i+1])])
#     return plainList


# def modularInverse(a, p):
#     for i in range(p+1):
#         if (i*a) % p == 1:
#             return i


# def decryption(cipherText, publicKey, privateKey):
#     cipherText = strToList(cipherText)
#     a = privateKey
#     g, h, p = publicKey
#     plaintext = []
#     for i in cipherText:
#         γ, δ = i
#         m = (((modularInverse(γ**a, p))) * (δ)) % p
#         plaintext.append(m)
#     plaintext = list_to_word(plaintext)
#     return plaintext


# plaintext = input("Enter plain text: ")
# p = int(input("Enter a prime number p: "))
# while not prime_chk(p) or p < 53:
#     if p < 53:
#         print("The value of p is too small. Please enter a larger number")
#     else:
#         print("The value you entered is not a prime number. Please enter a prime number.")
#     p = int(input("Enter a prime number for p: "))
# a = int(input("Enter private key a: "))
# publicKeys = [calc_g(p), (calc_g(p)**a) % p, p]
# print(f"The public key is {publicKeys}")
# print(f"The private key is {a}")
# print(f"Encrypted text: {encryption(plaintext,publicKeys)}")
# ciphertext = input("Enter cipher text: ")
# p = int(input("Enter prime number p: "))
# while not prime_chk(p) or p < 53:
#     if p < 53:
#         print("The value of p is too small. Please enter a larger number")
#     else:
#         print("The value you entered is not a prime number. Please enter a prime number.")
#     p = int(input("Enter a prime number for p: "))
# a = int(input("Enter prime number a: "))
# print(f"Decrypted text : {decryption(ciphertext,publicKeys,a)}\n\n\n\n")
