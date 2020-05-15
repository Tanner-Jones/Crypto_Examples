# Here is a simplified version of what is happening
# during the key exchange portion of the last example
# From sublimerobots.com with some minor adjustments

sharedPrime = 23
sharedBase = 5

aliceSecret = 6
bobSecret = 15

# Begin
print("Publicly Shared Variables:")
print("    Publicly Shared Prime: ", sharedPrime)
print("    Publicly Shared Base:  ", sharedBase)

# Alice Sends Bob A = g^a mod p
A = (sharedBase ** aliceSecret) % sharedPrime
print("\n  Alice Sends Over Public Chanel: ", A)

# Bob Sends Alice B = g^b mod p
B = (sharedBase ** bobSecret) % sharedPrime
print("\n Bob Sends Over Public Channel: ", B)

print("\n------------\n")
print("Privately Calculated Shared Secret:")
# Alice Computes Shared Secret: s = B^a mod p
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print("    Alice Shared Secret: ", aliceSharedSecret)

# Bob Computes Shared Secret: s = A^b mod p
bobSharedSecret = (A ** bobSecret) % sharedPrime
print("    Bob Shared Secret: ", bobSharedSecret)