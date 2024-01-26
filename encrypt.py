from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import os 
# def encrypt():
#     #load the public key
#     with open("public_key.pem", "rb") as key_file:
#         public_key = serialization.load_pem_public_key(
#             key_file.read(),
#         )


#     message = b"encrypted data"
#     ciphertext = public_key.encrypt(
#         message,
#         padding.OAEP(
#             mgf=padding.MGF1(algorithm=hashes.SHA256()),
#             algorithm=hashes.SHA256(),
#             label=None
#         )
#     )
#     print (ciphertext.hex())

#     with open('encryptedMessage.pem', 'wb') as pem_out:
#         pem_out.write(ciphertext)

#     return ciphertext

# encrypt()

def cipherText (file_data,public_key):
    return public_key.encrypt(
        file_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def encrypt_file(filename, public_key_pem_path):
    # Check if the file exists
    if not os.path.isfile(filename):
        print(f"File not found: {filename}")
        return
    
    # Check whether the file is of type .txt or .bmp
    if not (filename.endswith('.txt') or filename.endswith('.bmp')):
        print("Unsupported file type. Only .txt and .bmp files are accepted.")
        return
    
    # Load public key from PEM file
    with open(public_key_pem_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
        )

    # Check if the file is too large to encrypt with RSA
    if filename.endswith('.bmp'):
        max_data_size = (public_key.key_size // 8) - 66  # 66 bytes for OAEP padding with SHA-256

        # Read the contents of the file to be encrypted in binary mode
        encrypted_filename = "encrypted_" + filename

        # Read and encrypt the file
        with open(filename, 'rb') as file_to_encrypt, open(encrypted_filename, 'wb') as encrypted_file:
            file_data = file_to_encrypt.read()
            header, body = file_data[:54], file_data[54:]
            encrypted_file.write(header)

            # Process body in chunks
            for i in range(0, len(body), max_data_size):
                chunk = body[i:i+max_data_size]
                encrypted_chunk = cipherText(chunk, public_key)
                encrypted_file.write(encrypted_chunk)
        
        print(f"File encrypted successfully. Encrypted file: {encrypted_filename}")
        return encrypted_filename
    elif filename.endswith('.txt'):
        encrypted_filename_txt = "encrypted_" + filename
        with open(filename, 'rb') as file_txt :
            with open(encrypted_filename_txt, 'wb') as encrypted_file:
                file_data_txt = file_txt.read()
                fileText_Encrypted = cipherText(file_data_txt,public_key)
                encrypted_file.write(fileText_Encrypted)
    
    print(f"File encrypted successfully. Encrypted file: {encrypted_filename_txt}")
    return encrypted_filename_txt


#encrypt_file('./Lab-SSI/TextFile.txt', './Lab-SSI/public_key.pem')
#encrypt('./Lab-SSI/plaintext-ue.bmp', './Lab-SSI/public_key.pem')

### envoie du fichier encrypter par mail