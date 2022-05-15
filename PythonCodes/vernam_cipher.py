# Vernam Cipher

encrypted, decrypted = "", ""
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
plainText = (input("Enter plain text: ").replace(" ", "")).upper()
key = (input("Enter the encryption key: ").replace(" ", "")).upper()
if len(plainText) > len(key):
    for i in range(len(plainText) - len(key)):
        key += key[i]
for i in range(len(plainText)):
    encrypted += alphabet[(alphabet.index(key[i].upper()) -
                           alphabet.index(plainText[i].upper())) % 26]
print(f"The Encrypted text is {encrypted}")
encryptedText = (input("Enter the cipherText: ").replace(" ", "")).upper()
decryption_key = (input("Enter the encryption key: ").replace(" ", "")).upper()
if len(plainText) > len(decryption_key):
    for i in range(len(plainText) - len(decryption_key)):
        decryption_key += decryption_key[i]
for i in range(len(encryptedText)):
    decrypted += alphabet[(alphabet.index(decryption_key[i].upper()) -
                           alphabet.index(encryptedText[i].upper())) % 26]
print(f"The Decrypted text is {decrypted}")
