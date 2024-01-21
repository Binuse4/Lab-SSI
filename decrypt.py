from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

def decrypt_file(file_to_decrypt_name, private_key):
    # Load the private key
    with open(private_key, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )

    # Read the file to be decrypted content
    with open(file_to_decrypt_name, "rb") as file:
        ciphertext = file.read()

    # Décrypt
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Find the file extension to know if it is a text or bmp file
    if file_to_decrypt_name.endswith('.txt'):
        output_file_name = 'decrypted_'+ file_to_decrypt_name
    elif file_to_decrypt_name.endswith('.bmp'):
        output_file_name =  'decrypted_'+ file_to_decrypt_name
    else:
        raise ValueError("Type de fichier non supporté")

    # Save the decrypted file
    with open(output_file_name, 'wb') as file_out:
        file_out.write(plaintext)

    print(f'The file has been decreypted with the name : {output_file_name}')

