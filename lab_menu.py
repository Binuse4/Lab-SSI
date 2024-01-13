def menu( public_key_file , private_key_file):
    print("private key file :" + private_key_file )
    print("public key file :" + public_key_file )
    print("[1] Encrypt Message")
    print("[2] Decrypt Message")
    print("[3] Load public key file")
    print("[4] Load private key file")
    print("[5] Create and load new public and private key files")
    print("[6] Quit")

menu()
option = int(input ("Enter your option:"))

while option !=6:
    if option == 1:
        print("-1-")
    elif option == 2:
        print("-2-")
    elif option == 3:
        print("-3-")
    elif option == 4:
        print("-4-")
    elif option == 5:
        print("-5-")
    else:   
        print("Not an option!")   
    print()
    menu()
    option = int(input ("Enter your option:"))  
    
print("Exiting..see you next")