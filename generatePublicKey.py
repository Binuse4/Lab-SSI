from cryptography.hazmat.primitives import serialization

def generate_public_key(created_private_key_name , file_name):
    #load the private key
    with open(created_private_key_name, "rb") as key_file:
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
    with open(file_name, 'wb') as pem_out:
        pem_out.write(pem)
    
    print("The key was been well generated!")