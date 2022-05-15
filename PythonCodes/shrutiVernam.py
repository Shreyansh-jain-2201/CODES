def encrypt(p,k):
    l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kn=[]
    sum=[]
    f=[]
    i=0       
    for i in range(len(k)):
        sum.append((l.index(k[i])+l.index(p[i]))%26)
    c=""
    for x in sum:    
        c=c+l[x]
    print("Encrypted text: ",c)
def decrypt(cip,key):
    l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kn=[]
    sum=[]
    i=0       
    for i in range(len(key)):
        sum.append((l.index(cip[i])-l.index(key[i]))%26)
    c=""
    for x in sum:    
        c=c+l[x]
    print("Decrypted text: ",c)       
print("Enter plain text: ")
p=input("")
p=p.replace(" ","")
p=p.upper()
k=input("Enter key: ")
k=k.replace(" ","")
k=k.upper()
encrypt(p,k)
cip=input("Enter cipher text: ")
key=input("Enter key: ")
key=key.upper()
key=key.replace(" ","")
decrypt(cip,key)