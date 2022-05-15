import hmac
import hashlib
Key = input("Enter the secret key: ")
Key = b'{Key}'
message = input("Enter the message: ")
message = b'{message}'
digest_maker = hmac.new(Key, message, hashlib.sha1)
print("Hexdigest: " + digest_maker.hexdigest())
newMessage = input("Enter another message: ")
newMessage = b'{newMessage}'
digest_maker.update(newMessage)
print("Hexdigest after update: " + digest_maker.hexdigest())
print("Digest size: " + str(digest_maker.digest_size) + " bytes")
print("Block size: " + str(digest_maker.block_size) + " bytes")
print("Canonical name: " + digest_maker.name)
print("Digest: ", end=" ")
print(digest_maker.digest())
digest_clone = digest_maker.copy()
print("Hexdigest of clone: " + digest_clone.hexdigest())
