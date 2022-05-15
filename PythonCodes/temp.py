# import hashlib
# import base64
# from tinyec import registry
# import secrets
# from Crypto.Cipher import AES
# from Crypto import Random
# from advancedEncryptionStandards import *

# BLOCK_SIZE = 16
# def pad(s): return s + (BLOCK_SIZE - len(s) %
#                         BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)


# def unpad(s): return s[:-ord(s[len(s) - 1:])]


# def compress(pubKey):
#     return hex(pubKey.x) + hex(pubKey.y % 2)[2:]


# curve = registry.get_curve('brainpoolP256r1')
# alicePrivKey = secrets.randbelow(curve.field.n)
# alicePubKey = alicePrivKey * curve.g
# bobPrivKey = secrets.randbelow(curve.field.n)
# bobPubKey = bobPrivKey * curve.g
# aliceSharedKey = alicePrivKey * bobPubKey
# bobSharedKey = bobPrivKey * alicePubKey
# print("Equal shared keys:", aliceSharedKey == bobSharedKey)

# password = compress(aliceSharedKey)


# def encrypt(raw, password):
#     private_key = hashlib.sha256(password.encode("utf-8")).digest()
#     raw = pad(raw)
#     iv = Random.new().read(AES.block_size)
#     cipher = AES.new(private_key, AES.MODE_CBC, iv)
#     return base64.b64encode(iv + cipher.encrypt(raw.encode('utf-8')))


# def decrypt(enc, password):
#     private_key = hashlib.sha256(password.encode("utf-8")).digest()
#     enc = base64.b64decode(enc)
#     iv = enc[:16]
#     cipher = AES.new(private_key, AES.MODE_CBC, iv)
#     return unpad(cipher.decrypt(enc[16:]))


# # path = input(r'Enter path of Image : ')
# path = r'C:\Users\Shreyansh Jain\Downloads\wp4676584-4k-pc-wallpapers.jpg'
# fin = open(path, 'rb')
# image = fin.read()
# fin.close()
# image = base64.b64encode(image)
# image = str(image)
# # print(image)
# encryptedImage = encryption(image, password)
# print(encryptedImage)
# # decryptedImage = decryption(encryptedImage, password)
# # print(decryptedImage)
# # print(image == decryptedImage)
# # # print(encryptedImage)
# # print(password)
# # image = encrypt(image, password)
# # fin = open(path, 'wb')
# # fin.write(image)
# # fin.close()
# # fin = open(path, 'rb')
# # image = fin.read()
# # fin.close()
# # image = str(bytearray(image))
# # image = decrypt(image, password)
# # fin = open(path, 'wb')
# # fin.write(image)
# # fin.close()
import hashlib
import base64
from tinyec import registry
import secrets
from Crypto.Cipher import AES
from Crypto import Random
from advancedEncryptionStandards import *
BLOCK_SIZE = 16
def pad(s): return s + (BLOCK_SIZE - len(s) %
                        BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)


def unpad(s): return s[:-ord(s[len(s) - 1:])]


def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]


curve = registry.get_curve('brainpoolP256r1')
alicePrivKey = secrets.randbelow(curve.field.n)
alicePubKey = alicePrivKey * curve.g
bobPrivKey = secrets.randbelow(curve.field.n)
bobPubKey = bobPrivKey * curve.g
aliceSharedKey = alicePrivKey * bobPubKey
bobSharedKey = bobPrivKey * alicePubKey
print("Equal shared keys:", aliceSharedKey == bobSharedKey)

password = compress(aliceSharedKey)


def encrypt(raw, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode('utf-8')))


def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))


# path = input(r'Enter path of Image : ')
path = r'C:/Users/Shreyansh Jain/Downloads/ILTQq (1).png'
fin = open(path, 'rb')
image = fin.read()
fin.close()
image = base64.b64encode(image)
print(99, len(image))
# image = str(image.encode('utf-8'))
image = encryption(image, password)
print(1, image)
fin = open(path, 'wb')
fin.write(image)
fin.close()
fin = open(path, 'rb')
image = fin.read()
fin.close()
image = str(bytearray(image))
image = decrypt(image, password)
print(2, image)
fin = open(path, 'wb')
fin.write(image)
fin.close()
