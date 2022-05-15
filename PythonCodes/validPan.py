def check(panNo):
    if len(panNo) == 10 and panNo.isupper() and panNo[0:5].isalpha() and panNo[5:9].isdigit() and panNo[9].isalpha():
        return True
    return False


panNo = input()
if check(panNo):
    print("This is a valid pan card number.")
else:
    print("This is not a valid pan card number.")
