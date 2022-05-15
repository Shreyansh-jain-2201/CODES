

def decrypt(cip):
    alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    c=[]
    frequencylist="ETAOINSHRDLCUNWFGYPBVKJXQZ"
    i=0
    for i in range(len(alpha)):
        c.append(cip.count(alpha[i]))
    maxoccur=0
    j=0
    for j in range(len(c)):
        if(c[j]>maxoccur):
            maxoccur=c[j]
            maxalpha_pos=j
    key=(maxalpha_pos - alpha.index(frequencylist[0]))%26
    output=""
    for x in cip:
        output+=alpha[(alpha.index(x)-key)%26]
    print(output)    
    choice=input("Is the text understandable?(YES/NO): ")
    choice=choice.upper()
    if choice == "YES":
        return f"The key is {key}"
    i=1;
    while(choice=="NO"):
         output=""
         key=(maxalpha_pos - alpha.index(frequencylist[i]))%26
         for x in cip:
            output+=alpha[(alpha.index(x)-key)%26]
         print(output)
         choice=input("Is the text understandable?(YES/NO): ")
         choice=choice.upper()
         i+=1
    return f"The key is {key}"


cipher=input("Cipher text: ")
print(decrypt(cipher))

