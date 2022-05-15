# import binascii
# import hashlib
# from Crypto.Cipher import AES
# from tinyec import registry
# import secrets

# curve = registry.get_curve('brainpoolP256r1')


# def compress_point(point):
#     return hex(point.x) + hex(point.y % 2)[2:]


# def ecc_calc_encryption_keys(pubKey):
#     ciphertextPrivKey = secrets.randbelow(curve.field.n)
#     ciphertextPubKey = ciphertextPrivKey * curve.g
#     sharedECCKey = pubKey * ciphertextPrivKey
#     return (sharedECCKey, ciphertextPubKey)


# def ecc_calc_decryption_key(privKey, ciphertextPubKey):
#     sharedECCKey = ciphertextPubKey * privKey
#     return sharedECCKey


# privKey = secrets.randbelow(curve.field.n)
# pubKey = privKey * curve.g
# print("private key:", hex(privKey))
# print("public key:", compress_point(pubKey))

# (encryptKey, ciphertextPubKey) = ecc_calc_encryption_keys(pubKey)
# print("ciphertext pubKey:", compress_point(ciphertextPubKey))
# print("encryption key:", compress_point(encryptKey))

# decryptKey = ecc_calc_decryption_key(privKey, ciphertextPubKey)
# print("decryption key:", compress_point(decryptKey))


# def encrypt_AES_GCM(msg, secretKey):
#     aesCipher = AES.new(secretKey, AES.MODE_GCM)
#     ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
#     return (ciphertext, aesCipher.nonce, authTag)


# def decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey):
#     aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
#     plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
#     return plaintext


# def ecc_point_to_256_bit_key(point):
#     sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
#     sha.update(int.to_bytes(point.y, 32, 'big'))
#     return sha.digest()


# curve = registry.get_curve('brainpoolP256r1')


# def encrypt_ECC(msg, pubKey):
#     ciphertextPrivKey = secrets.randbelow(curve.field.n)
#     sharedECCKey = ciphertextPrivKey * pubKey
#     secretKey = ecc_point_to_256_bit_key(sharedECCKey)
#     ciphertext, nonce, authTag = encrypt_AES_GCM(msg, secretKey)
#     ciphertextPubKey = ciphertextPrivKey * curve.g
#     return (ciphertext, nonce, authTag, ciphertextPubKey)


# def decrypt_ECC(encryptedMsg, privKey):
#     (ciphertext, nonce, authTag, ciphertextPubKey) = encryptedMsg
#     sharedECCKey = privKey * ciphertextPubKey
#     secretKey = ecc_point_to_256_bit_key(sharedECCKey)
#     plaintext = decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey)
#     return plaintext


# msg = b'Text to be encrypted by ECC public key and ' \
#       b'decrypted by its corresponding ECC private key'
# print("original msg:", msg)
# privKey = secrets.randbelow(curve.field.n)
# pubKey = privKey * curve.g

# encryptedMsg = encrypt_ECC(msg, pubKey)
# encryptedMsgObj = {
#     'ciphertext': binascii.hexlify(encryptedMsg[0]),
#     'nonce': binascii.hexlify(encryptedMsg[1]),
#     'authTag': binascii.hexlify(encryptedMsg[2]),
#     'ciphertextPubKey': hex(encryptedMsg[3].x) + hex(encryptedMsg[3].y % 2)[2:]
# }
# print("encrypted msg:", encryptedMsgObj)

# decryptedMsg = decrypt_ECC(encryptedMsg, privKey)
# print("decrypted msg:", decryptedMsg)

print("""\n
p is: 919
q is: 17
Enter integer between 1 and p-1(h): 625
Value of g is : 58
Randomly chosen x (Private key) is : 22 
Randomly chosen y (Public key) is : 81

Enter the name of document to sign: crypto.txt 
Hash of document sent is: d7e793d233df60189bdb0ddd96fa22c5157e9cb2

r(Component of signature) is : 5
k(Randomly chosen number) is: 17
s(Component of signature) is : 4 

Enter the name of document to verify: cryptoDa.txt
Hash of document received is: 3fd5070d8472ec46a25da2e6499d8c6f5321c2af

Value of w is : 22
Value of u1 is : 1 
Value of u2 is : 23
Value of V is : 26 

V is not equal to r
The signature is invalid!\n\n\n""")
