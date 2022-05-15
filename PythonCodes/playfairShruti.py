# Playfair Cipher

def keySquare(key):
    key = key.upper()
    key = key.replace(" ", "")
    alphabets = key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    alphabets.lower()
    list1 = []
    output = []
    for i in alphabets:
        if not i in list1 and i != "J":
            list1.append(i)
    for i in range(5):
        rows = []
        for j in range(5):
            rows.append(list1[0])
            list1.pop(0)
        output.append(rows)
    return output


def bogusElement(plaintext):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    plaintext = list(plaintext.upper())
    if not "X" in plaintext:
        return "X"
    else:
        for i in reversed(alphabets):
            if not i in plaintext:
                return i


def createPair(plaintext, bogus):
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(" ", "")
    output = []
    for i in range(0, len(plaintext) + 1, 2):
        try:
            if plaintext[i] == plaintext[i+1]:
                plaintext = plaintext[0:i+1] + bogus + plaintext[i+1:]
        except:
            continue
    for i in range(0, len(plaintext), 2):
        try:
            output.append(plaintext[i] + plaintext[i+1])
        except:
            output.append(plaintext[i] + bogus)
    return output


def location(letter, key):
    if letter == "J":
        letter = "I"
    for i in keySquare(key):
        if letter in i:
            x = keySquare(key).index(i)
            return f"[{x}][{i.index(letter)}]"


def ifSameRow(pair, key):
    index1 = location(pair[0], key)
    index2 = location(pair[1], key)
    if index1[1] == index2[1]:
        return True
    else:
        return False


def ifSameCol(pair, key):
    index1 = location(pair[0], key)
    index2 = location(pair[1], key)
    if index1[4] == index2[4]:
        return True
    else:
        return False


def sameRowOperation(pair, key):
    letter1 = location(pair[0], key)
    first1 = int(letter1[1])
    first2 = int(letter1[4])
    letter2 = location(pair[1], key)
    second1 = int(letter2[1])
    second2 = int(letter2[4])
    list1 = keySquare(key)
    output = list1[first1][(first2 + 1) % 5] + \
        list1[second1][(second2 + 1) % 5]
    return output


def sameColOperation(pair, key):
    letter1 = location(pair[0], key)
    first1 = int(letter1[1])
    first2 = int(letter1[4])
    letter2 = location(pair[1], key)
    second1 = int(letter2[1])
    second2 = int(letter2[4])
    list1 = keySquare(key)
    output = list1[(first1 + 1) % 5][first2] + \
        list1[(second1 + 1) % 5][second2]
    return output


def rectangleOperation(pair, key):
    letter1 = location(pair[0], key)
    first1 = int(letter1[1])
    first2 = int(letter1[4])
    letter2 = location(pair[1], key)
    second1 = int(letter2[1])
    second2 = int(letter2[4])
    list1 = keySquare(key)
    output = list1[first1][second2] + list1[second1][first2]
    return output


def Encrypt(plaintext, key):
    matrix = keySquare(key)
    bogus = bogusElement(plaintext)
    pairs = createPair(plaintext, bogus)
    output = ""
    for pair in pairs:
        if ifSameCol(pair, key) and ifSameRow(pair, key):
            pair[0], pair[1] = pair[1], pair[0]
            output += pair
        elif ifSameRow(pair, key):
            output += sameRowOperation(pair, key)
        elif ifSameCol(pair, key):
            output += sameColOperation(pair, key)
        else:
            output += rectangleOperation(pair, key)
    return output


def NewSameRowOperation(pair, key):
    letter1 = location(pair[0], key)
    first1 = int(letter1[1])
    first2 = int(letter1[4])
    letter2 = location(pair[1], key)
    second1 = int(letter2[1])
    second2 = int(letter2[4])
    list1 = keySquare(key)
    output = list1[first1][(first2 - 1) % 5] + \
        list1[second1][(second2 - 1) % 5]
    return output


def NewSameColOperation(pair, key):
    letter1 = location(pair[0], key)
    first1 = int(letter1[1])
    first2 = int(letter1[4])
    letter2 = location(pair[1], key)
    second1 = int(letter2[1])
    second2 = int(letter2[4])
    list1 = keySquare(key)
    output = list1[(first1 - 1) % 5][first2] + \
        list1[(second1 - 1) % 5][second2]
    return output


def Decrypt(encrypted_text, key):
    matrix = keySquare(key)
    bogus = bogusElement(encrypted_text)
    pairs = createPair(encrypted_text, bogus)
    output = ""
    final_output = ""
    for pair in pairs:
        if ifSameCol(pair, key) and ifSameRow(pair, key):
            pair[0], pair[1] = pair[1], pair[0]
            output += pair
        elif ifSameRow(pair, key):
            output += NewSameRowOperation(pair, key)
        elif ifSameCol(pair, key):
            output += NewSameColOperation(pair, key)
        else:
            output += rectangleOperation(pair, key)
    for i in output:
        if i != bogus:
            final_output += i
    output = final_output
    return output


plaintext = input("Enter the text you want to Encrypt: ")
key = input("Enter the key: ")
print(f"The encrypted text is: {Encrypt(plaintext,key)}")

encrypted_text = input("Enter the encrypted text: ")
decryption_key = input("Enter the decryption key: ")
print(f"The decrypted text is: {Decrypt(encrypted_text,decryption_key)}")
