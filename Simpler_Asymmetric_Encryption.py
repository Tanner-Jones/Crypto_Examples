# Example of the importance of Asymmetric Encryption
# This is a simplified example of the RSA encryption method
# Math pulled from https://www.onebigfluke.com/2013/11/public-key-crypto-math-explained.html
# Modular functionsfrom https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm

def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

def modinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g != 1:
        raise Exception('gcd(a, b) != 1')
    return x % b

def encrypt(message,a,b):
    encrypted_message = message**a % b
    return encrypted_message

def decrypt(message,c,d):
    decrypted_message = message**c % d
    return decrypted_message

p = 7                       # Pick two prime numbers
q = 13
n = p * q                   # Multiply them together
phi = (p - 1) * (q - 1)     # Euler's totient is implemented
e = 23                      # e = 1 < e < phi and shares no common factors wit phi
d = modinv(e, phi)          # the modular multiplicative inverse


print("Now our private key pair = " + str(n) + " and " + str(d))
print("And our public key pair = " + str(n) + " and " + str(e))
print("Imagine these both belong to Bob, but Bob only shares his public key with Alice \n")

message = 89
enc_message = encrypt(message, e, n)
print("Alice, after encrypting her message with Bob's public key, send him: " + str(enc_message))
dec_message = decrypt(enc_message, d, n)
print("Bob, uses his private key, and decodes: " + str(dec_message) + "\n")


print("Bob can also use his key pair to authenticate his messages")
message = 23
enc_message = encrypt(message, d, n)
print("Bob sends his encrypted message to Alice: " + str(enc_message))
dec_message = decrypt(enc_message, e, n)
print("Alice decodes the message using Bob's public key: " + str(dec_message))
print("Alice now knows that it is for sure Bob sending that message because only his public key works to decode it")
