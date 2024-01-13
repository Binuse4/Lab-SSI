from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import  padding
from cryptography.hazmat.primitives import hashes
from encrypt import *


#load the private key
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )

ciphertext = encrypt()

plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print('Le texte')
print (plaintext)

with open('decryptedMessage.pem', 'wb') as pem_out:
        pem_out.write(plaintext)