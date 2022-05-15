def sum(num):
    output = 0
    for i in str(num):
        output += int(i)
    return output

# n = int(input(""))
# for i in range(n):
#     s = input("")
#     num = input("")
#     while len(str(num)) > 1 and not isEbne(num):
#         if isEven(num):
#             num = num[0:-1]
#         if not isEbne(num) and not isEven(num):
#             for i in range(len(str(num))):
#                 try:
#                     if not isEven(num[i]):
#                         num = num[0:i] + num[i+1:]
#                         break
#                 except:
#                     continue
#         if isEbne(num):
#             break
#     if not len(str(num)) or not isEbne(num):
#         print(-1)
#     else:
#         print(int(num))


n = int(input(""))
for i in range(n):
    s = input("")
    num = input("")
    p = 1
    while (not int(num)%2 == 0 or not sum(num)%2) and p:
        num = str(num[0:-1])
        if len(num) <=1:
            p = 0
    if int(num)%2 == 0 and sum(num)%2 == 0:
        print(num)
    else:
        print(num)
    