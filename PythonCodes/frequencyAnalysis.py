# Frequency Analysis

def analyse_the_text(ciphertext):
    frequencylist = list("ETAOINSHRDLCUNWFGYPBVKJXQZ")
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    most_frequent_letter = ''
    frequency = 0
    for i in alphabet:
        if ciphertext.count(i)>frequency:
            frequency = ciphertext.count(i)
            most_frequent_letter = i
    key = (alphabet.index(most_frequent_letter) - alphabet.index(frequencylist[0]))%26
    output = ""
    for i in ciphertext:
        output += alphabet[(alphabet.index(i) - key)%26]
    print(output)
    if_correct = input("Is the text understandable?(Y/N): ").upper()
    if if_correct == "N":
        for i in range(1,26,1):
            key = (alphabet.index(most_frequent_letter) - alphabet.index(frequencylist[i]))%26
            output = ""
            for i in ciphertext:
                output += alphabet[(alphabet.index(i) - key)%26]
            print(output)
            if_correct = input("Is the text understandable?(Y/N): ").upper()
            if if_correct == "Y":
                break
    
    return f"The key is {key}"

ciphertext = input("Enter the text you want to decipher: ")
print(analyse_the_text(ciphertext))

