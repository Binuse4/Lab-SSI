from cryptography.hazmat.primitives import serialization
#load the private key
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
    )


public_key = private_key.public_key()
pem = public_key.public_bytes(
   encoding=serialization.Encoding.PEM,
   format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Write the PEM format key to a file
with open('public_key.pem', 'wb') as pem_out:
    pem_out.write(pem)