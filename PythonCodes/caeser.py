alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

plaintext = input("Enter the plaintext: ").upper()
key = int(input("Enter the key: "))

ciphertext = ""
for i in plaintext:
    ciphertext += alphabets[(alphabets.index(i) + key) % 26]

print(f"The ciphertext is {ciphertext}.")

ciphertext = input("Enter the ciphertext: ")
decryption_key = int(input("Enter the decryption key: "))

plaintext = ""
for i in ciphertext:
    plaintext += alphabets[(alphabets.index(i) - key) % 26]

print(f"The original plaintext is {plaintext}.")
