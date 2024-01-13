from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import  padding
from cryptography.hazmat.primitives import hashes

def encrypt():
    #load the public key
    with open("public_key.pem", "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
        )


    message = b"encrypted data"
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print (ciphertext.hex())

    with open('encryptedMessage.pem', 'wb') as pem_out:
        pem_out.write(ciphertext)

    return ciphertext

encrypt()