# This is the realistic example of asymmetric encryption. The importance of asymmetric encryption is being able to
# share secure communication with anyone, including people you have not previously shared secrets(keys) with.
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

private_key = rsa.generate_private_key(                 # generates a private key to use
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()                   # derives a public key from previously generated private key

message = b'Hi Bob this is Alice, I will be sending you a message using your public key'


encrypted = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print(encrypted)                                        # Our now encrypted message

original_message = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(original_message)                                 # The successfully decrypted message using private key


