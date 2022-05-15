def countA(word):
    count = 0
    for i in word:
        if i == 'a':
            count += 1
    return count

word = input("")
# print(countA("ababababababababababababababababababababababababav"))
# print(len("ababababababababababababababababababababababababav"))
if 2 *countA(word) > len(word):
    print(len(word))
else:
    print(2 * countA(word) - 1)



for i in range(256):
    print(chr(i))