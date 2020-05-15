from cryptography.fernet import Fernet

# Let's begin by showing an example of what encryption looks like

# This is an example random key. If you run the file again
# you will notice the key is different each time
key = Fernet.generate_key()
print(key)

# Fernet is just a symmetric encryption implementation
f = Fernet(key)
print(f)

# Notice the Encrypted output of this example string
# You don't need to worry about how the message is being encrypted
# Just notice that the output is gibberish compared to the input
token = f.encrypt(b"This is some example of a secret")
print(token)

# an accompanying decryption is established
token = f.decrypt(token)
print(token)

