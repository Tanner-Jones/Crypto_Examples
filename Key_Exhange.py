from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF


# Let's look at some example code from the Cryptography library to
# illustrate the Diffie-Hellman exchange
# For now ignore a good portion of what is happening inside this code
# what is important to understand is the process this is used for

# Generate some parameters. These can be reused.
parameters = dh.generate_parameters(generator=2, key_size=2048,
                                    backend=default_backend())

# Generate a private key for use in the exchange.
server_private_key = parameters.generate_private_key()
# In a real handshake the peer is a remote client. For this
# example we'll generate another local private key though. Note that in
# a DH handshake both peers must agree on a common set of parameters.
# This agreement is often called a handshake, in which the encryption
# options of both parties are discussed and then one is chosen
peer_private_key = parameters.generate_private_key()
shared_key = server_private_key.exchange(peer_private_key.public_key())
# Perform key derivation.
derived_key = HKDF(
     algorithm=hashes.SHA256(),
     length=32,
     salt=None,
     info=b'handshake data',
     backend=default_backend()
).derive(shared_key)
# And now we can demonstrate that the handshake performed in the
# opposite direction gives the same final value
same_shared_key = peer_private_key.exchange(
      server_private_key.public_key()
)
same_derived_key = HKDF(
     algorithm=hashes.SHA256(),
     length=32,
     salt=None,
     info=b'handshake data',
     backend=default_backend()
).derive(same_shared_key)
print(derived_key)
print(same_derived_key)
