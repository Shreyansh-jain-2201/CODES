while(1):
    choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT\n"))
    if choice:
        pt = input('Enter the plain text:') 
        key = input("Enter Key:")
        print("\n")
        print("Encryption")
        cipher_text = bin2hex(encrypt(pt, rkb, rk))
        print("Cipher Text : ",cipher_text)
    elif choice==2:
		cipher_text = input('Enter the Cipher text:')
		key = input("Enter Key:")
		print("\n")
		print("Decryption")
		rkb_rev = rkb[::-1]
		rk_rev = rk[::-1]
		text = bin2hex(encrypt(cipher_text, rkb_rev, rk_rev))
		print("Plain Text : ",text)
	elif choice==3:
		exit()
	
	else:
		print("Choose a valid option: ")