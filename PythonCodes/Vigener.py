# Vigenere Cipher

def encryption(plaintext, key):
    if len(plaintext) > len(key):
        n = len(plaintext) - len(key)
        for i in range(n):
            key += key[i]
    else:
        n = len(key) - len(plaintext)
        for i in range(n):
            plaintext += key[i]
    alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    output = ""
    for i in range(len(plaintext)):
        output += alphabets[(alphabets.index(key[i]) -
                             alphabets.index(plaintext[i])) % 26]
    return output


def decryption(ciphertext, key):
    if len(ciphertext) > len(key):
        n = len(ciphertext) - len(key)
        for i in range(n):
            key += key[i]
    else:
        n = len(key) - len(ciphertext)
        for i in range(n):
            ciphertext += key[i]
    alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    output = ""
    for i in range(len(ciphertext)):
        output += alphabets[(alphabets.index(key[i]) -
                             alphabets.index(ciphertext[i])) % 26]
    return output


plaintext = (input("Enter plain text: ").replace(" ", "")).upper()
key = (input("Enter the encryption key: ").replace(" ", "")).upper()
print(f"The Encrypted text is {encryption(plaintext,key)}")
ciphertext = (input("Enter the ciphertext: ").replace(" ", "")).upper()
key = (input("Enter the decryption key: ").replace(" ", "")).upper()
print(f"The Decrypted text is {decryption(ciphertext,key)}")
