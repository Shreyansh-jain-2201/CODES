def numToText(num):
    numToAlp = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L',
                12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
                23: 'X', 24: 'Y', 25: 'Z', 26: 'a', 27: 'b', 28: 'c', 29: 'd', 30: 'e', 31: 'f', 32: 'g', 33: 'h',
                34: 'i', 35: 'j', 36: 'k', 37: 'l', 38: 'm', 39: 'n', 40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's',
                45: 't', 46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y', 51: 'z', 52: ' '}
    output = ""
    for i in num:
        output += numToAlp[i % 26]
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


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


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


def modulusConst(p, q):
    return p*q


def eulerTotient(p, q):
    return (p-1) * (q-1)


def eulerConstant(p, q):
    for i in range(2, eulerTotient(p, q)):
        if gcd(i, eulerTotient(p, q)) == 1:
            return i
    return -1


def multiplicativeInverse(p, q, e):
    n = eulerTotient(p, q)
    # e = eulerConstant(p, q)
    for i in range(n+1):
        if (e*i) % n == 1:
            return i
    return -1


def publicKey(p, q):
    e = eulerConstant(p, q)
    n = modulusConst(p, q)
    return [e, n]


def privateKey(p, q, e):
    # e = eulerConstant(p, q)
    d = multiplicativeInverse(p, q, e)
    n = modulusConst(p, q)
    return [d, n]


def strToList(list1):
    list1 = list1.split(",")
    output = []
    for i in range(len(list1)):
        if i == 0:
            output.append(int(list1[i][1:]))
        elif i == len(list1) - 1:
            output.append(int(list1[i][:-1]))
        else:
            output.append(int(list1[i]))
    return output


def encryption(plaintext, publicKey, e):
    plaintext = textToNum(plaintext)
    x, n = publicKey
    ciphertext = []
    for i in plaintext:
        ciphertext.append((i**e) % n)
    return ciphertext


def decryption(ciphertext, privateKey):
    d, n = privateKey
    plaintext = []
    ciphertext = strToList(ciphertext)
    for i in ciphertext:
        plaintext.append((i**d) % n)
    plaintext = numToText(plaintext)
    return plaintext


# plaintext = input("Enter the text you want to encrypt: ")
# p = int(input("Enter a prime number for p: "))
# while not checkPrime(p):
#     print("The value you entered is not a prime number. Please enter a prime number.")
#     p = int(input("Enter a prime number for p: "))
# q = int(input("Enter a prime number for q: "))
# while not checkPrime(q):
#     print("The value you entered is not a prime number. Please enter a prime number.")
#     q = int(input("Enter a prime number for q: "))
# publicKey = publicKey(p, q)
# privateKey = privateKey(p, q)
# print(f"The value of RSA Modulus(n) is : {modulusConst(p,q)}")
# print(f"The value of Euler's Totient (φ(n)) is : {eulerTotient(p,q)}")
# e = int(input("Enter the value of Euler: "))
# print(f"The value of e is : {eulerConstant(p,q)}")
# print(f"The value of d is : {multiplicativeInverse(p,q)}")
# print(f"The Public keys are : {publicKey[0], publicKey[1]}")
# print(f"The Private keys are : {privateKey[0], privateKey[1]}")
# print(f"The Encrypted text is : {encryption(plaintext, publicKey, e)}")
ciphertext = input("Enter the text you want to decrypt: ")
p = int(input("Enter a prime number for p: "))
while not checkPrime(p):
    print("The value you entered is not a prime number. Please enter a prime number.")
    p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))
while not checkPrime(q):
    print("The value you entered is not a prime number. Please enter a prime number.")
    q = int(input("Enter a prime number for q: "))
e = int(input("Enter the value of Euler: "))
# privateKey = privateKey(p, q)
print(
    f"The original plaintext is: {decryption(ciphertext, privateKey(p,q, e))}")


# [46, 77, 30, 69]
