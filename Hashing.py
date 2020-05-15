from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from bitstring import BitArray

# Hashes are a method to authenticate that a message that was sent
# has not been tampered with. It is essentially an irreversible
# encryption that is unique to the message that is sent. So
# if somehow the original message were to be tempered with, Alice
# could send a hash of her message to Bob and Bob could hash the message
# he received in order to verify the hashes are the same

digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(b"Here is the message I want to send")
digest.update(b"This is some additional information to add to my message")
first_digest = digest.finalize()
print(first_digest)

# Observe what was printed to the terminal for from the above print statement and look at the next bit of code.
# Here we are only adding one character to the message from before but you can see in the terminal output
# that the corresponding hash is completely different.
# The additional bit of code is to again demonstrate that the hash remains exactly the same until we add or remove from
# it

digest2 = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest2.update(b"Here is the message I want to send")
digest2.update(b"This is some additional information to add to my messagd")
digest3 = digest2.copy()
digest2.update(b"h")
print(digest2.finalize())


first_digest_bits = ''.join(format(byte, '08b') for byte in first_digest)
second_digest = digest3.finalize()
second_digest_bits = ''.join(format(byte, '08b') for byte in second_digest)
print(first_digest_bits)
print(second_digest_bits)
print(len(first_digest_bits))
Changed_sum = 0
for i in range(0,len(first_digest_bits)):
    if first_digest_bits[i] == second_digest_bits[i]:
        Changed_sum = Changed_sum + 1

print(Changed_sum)
