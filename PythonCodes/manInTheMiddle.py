# def checkPrime(num):
#     counter = 1
#     for i in range(2, num+1):
#         if i**2 <= num+1:
#             if num%i == 0:
#                 counter = 0
#                 break
#             else:
#                 continue
#         else:
#             break
    
#     if counter == 1:
#         return True
#     else:
#         return False
    
# def calculatePrimitiveRoot(num):
#     for i in range(1, num):
#         roots = set()
#         for j in range(1, num):
#             if (i**j)%num:
#                 roots.add((i**j)%num)
#         if len(list(roots)) == num - 1:
#             return i

# def calculatePublicKey(p, secretKey):
#     return (calculatePrimitiveRoot(p)**secretKey)%p


# p = int(input("Enter a prime number: "))
# print(f"The primitive root(g) of {p} is {calculatePrimitiveRoot(p)}")
# x_sergio = int(input("Enter Sergio's private key: "))
# y_sergio = calculatePublicKey(p, x_sergio)
# print(f"Sergio computed his Public key: {y_sergio}")
# x_berlin = int(input("Enter Berlin's private key: "))
# y_berlin = calculatePublicKey(p, x_berlin)
# print(f"Berlin computed his Public key: {y_berlin}")
# print("""
# A malicious third party, Prieto, is able to perform a Man in the middle attacks on the conversation between Sergio and Berlin.
#       """)
# x_prieto_sergio = int(input("Enter Prieto's private key for Sergio: "))
# y_prieto_sergio = calculatePublicKey(p, x_prieto_sergio)
# print(f"Prieto computed his Public key for Sergio: {y_prieto_sergio}")
# key_sergio_pierto = (y_sergio ** x_prieto_sergio)%p
# print(f"Pierto computed the secret key for Sergio: {key_sergio_pierto}")
# key_sergio = (y_prieto_sergio ** x_sergio)%p
# print(f"Sergio computed his secret key: {key_sergio}")
# x_prieto_berlin = int(input("Enter Prieto's private key for Berlin: "))
# y_prieto_berlin = calculatePublicKey(p, x_prieto_berlin)
# print(f"Prieto computed his Public key for Berlin: {y_prieto_berlin}")
# key_berlin_pierto = (y_berlin ** x_prieto_berlin)%p
# print(f"Pierto computed the secret key for Berlin: {key_berlin_pierto}")
# key_berlin = (y_prieto_berlin ** x_berlin)%p
# print(f"Berlin computed his secret key: {key_berlin}")
# print("\n__________Man in the middle attack carried out successfully.__________\n")





def prime_chk(n):
    f=0
    for i in range(1,n):
        if(n%i==0):
            f=f+1
    if(f==2 or n!=1):
        return True
    else:
        return False
def calc_alpha(n):
    for i in range(1,n):
        l=[]
        for j in range(1,n):
            if ((i**j)%n):
                l.append((i**j)%n)
        s=list(set(l))
        if(len(s)==n-1):
            return i
def public_key(n,a):
    pk=(calc_alpha(n)**a)%n
    return pk
p=int(input("Enter a prime number p: "))
print(f"The primitive root(g) of p is: {calc_alpha(p)}")
npk=int(input("Enter Nairobi's private key: "))
tpk=int(input("Enter Tokyo's private key: "))
print('''\n\nA thirdparty, Raquel, is able to modify messages between Nairobi and Tokyo. Raquel knows P the prime number, and g the primitive \nroot modulo\n\n''')
rpkn=int(input("Raquel chose private key for Nairobi: "))
print(f"Raquel sent her public key to Nairobi as : {public_key(p,rpkn)}")
print(f"Nairobi sent her public key to Raquel as :{public_key(p,npk)}")
ckrn=(public_key(p,rpkn)**npk)%p
ckn = (public_key(p, npk) ** rpkn)%p
print(f"Raquel computed secret key for Nairobi: {ckrn}")
print(f"Nairboi computed her secret key: {ckn}")
rpkt=int(input("Raquel chose private key for Tokyo: "))
print(f"Raquel sent her public key to Tokyo as : {public_key(p,rpkt)}")
print(f"Tokyo sent her public key to Raquel as :{public_key(p,tpk)}")
ckrt=(public_key(p,rpkt)**tpk)%p
ckt =(public_key(p,tpk)**rpkt)%p
print(f"Raquel and Tokyo computed common key as: {ckrt}")
print(f"Tokyo computed her secret key: {ckt}")
print("\n\nThus the man in the middle attack is successfully achieved!\n\n")
