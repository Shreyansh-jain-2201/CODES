from Crypto.PublicKey import RSA


def transaction(enum, ename, edate, ecvv, k):
    dnum = []
    dname = []
    ddate = []
    dcvv = []
    for i in range(0, len(enum)):
        dnum.append(enum[i]-k)
    for i in range(0, len(ename)):
        dname.append(ename[i]-k)
    for i in range(0, len(edate)):
        ddate.append(edate[i]-k)
    for i in range(0, len(ecvv)):
        dcvv.append(ecvv[i]-k)
    for i in range(0, len(dnum)):
        dnum[i] = chr(dnum[i])
    for i in range(0, len(dname)):
        dname[i] = chr(dname[i])
    for i in range(0, len(ddate)):
        ddate[i] = chr(ddate[i])
    for i in range(0, len(dcvv)):
        dcvv[i] = chr(dcvv[i])
    dnum = convert(dnum)
    dname = convert(dname)
    ddate = convert(ddate)
    dcvv = convert(dcvv)
    password = input("Enter the password: ")
    if(password == 'password'):
        return 1
    else:
        print("Incorrect Password!")
        return 0


def convert(s):
    new = ""
    for x in s:
        new += x
    return new


print("Enter the Card Type: ")
print("1. Visa.")
print("2. Mastercard.")
print("3. American Express.")
print("4. RuPay.")
enum = []
ename = []
edate = []
ecvv = []
cardtype = int(input())
num = int(input(("Enter the card number: ")))
num = str(num)
if(len(num) != 12):
    print("Invalid Number.")
    num = int(input("Enter the correct number: "))
    num = str(num)
name = input("Enter the card holder's name: ")
date = int(input("Enter the date mmyy: "))
date = str(date)
if(len(date) != 4):
    print("Invalid date.")
    date = int(input("Enter correct date: "))
    date = str(date)
cvv = int(input("Enter the cvv number: "))
cvv = str(cvv)
if(len(cvv) != 3):
    print("Invalid cvv.")
    cvv = int(input("Enter the correct cvv number: "))
k = 2
for i in range(0, len(num)):
    enum.append(ord(num[i])+k)
for i in range(0, len(name)):
    ename.append(ord(name[i])+k)
for i in range(0, len(date)):
    edate.append(ord(date[i])+k)
for i in range(0, len(cvv)):
    ecvv.append(ord(cvv[i])+k)
if(transaction(enum, ename, edate, ecvv, k)):
    print("The transaction was successful.")
else:
    print("Sorry! The transaction was unsuccessful.")

# key = RSA.generate(2048)
# private_key = key.export_key(passphrase="your-passphrase")
# filename = input("Enter filename to store private key:")
# file_out = open(filename, "wb")
# file_out.write(private_key)
# file_out.close()
# public_key = key.publickey().export_key()
# filename2 = input("Enter filename to store public key:")
# file_out = open(filename2, "wb")
# file_out.write(public_key)
# file_out.close()
# print(public_key)
