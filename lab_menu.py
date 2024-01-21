from generatePrivateKey import *;
from generatePublicKey import *;
from decrypt import decrypt_file;

def menu( public_key_file , private_key_file):
    print("private key file :" + private_key_file )
    print("public key file :" + public_key_file )
    print("[1] Encrypt Message")
    print("[2] Decrypt Message")
    print("[3] Load public key file")
    print("[4] Load private key file")
    print("[5] Create and load new public and private key files")
    print("[6] Quit")


public_key_file = "None"
private_key_file= "None"
menu(public_key_file, private_key_file)
option = int(input ("Enter your option:"))

while option !=6:
    if option == 1:
        print("-1-")
    elif option == 2:
        print("-2- Decrypt message")
        file_to_decrypt_name = input("Enter the name of the file(BMP or Text File) you want to decrypt with it extension (ex :my_file_to_be_decrypted.bmp): ")
        decrypt_file(file_to_decrypt_name, private_key_file )
    elif option == 3:
        print("-3- Load public key file")
        public_file_name = input("Enter the name of the public key file (my_public_key.pem): ")
        public_key_file = public_file_name
    elif option == 4:
        print("-4- Load private key file")
        private_file_name = input("Enter the name of the private key file (my_private_key.pem): ")
        private_key_file = private_file_name
    elif option == 5:
        print("-5- Create and load new public and private key files")
        private_file_name = input("Enter the name of the private key file (my_private_key.pem): ")
        public_file_name = input("Enter the name of the public key file (my_public_key.pem): ")
        public_key_file = public_file_name
        private_key_file = private_file_name
        generate_private_key(private_file_name) 
        generate_public_key(private_file_name , public_file_name)

    else:   
        print("Not an option!")   
    print()
    menu(public_key_file, private_key_file)
    option = int(input ("Enter your option:"))  
    
print("Exiting..see you next")