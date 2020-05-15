# This module will demonstrate a simpler encryption method to show what might be happening during encryption and
# decryption processes. Some knowledge of ASCII is required, simply looking up the ASCII table will suffice.


def encrypt(message, key):
    example_message_characters = list(message)                  # Breaks down message into list of it's characters
    print(example_message_characters)

    ascii_values = [ord(c) for c in example_message_characters] # Converts each character to it's ASCII value
    print(ascii_values)

    # Our encryption will run an exclusive or operation on the key and each character. The nature of exclusive or
    # allows for one function to both encrypt and decrypt
    encryption = [c ^ key for c in ascii_values]
    print(encryption)
    encrypted_characters = [chr(c) for c in encryption]
    encrypted_message = "".join(encrypted_characters)
    return encrypted_message


# Try looking through this code to understand what exactly is happening and you will get a good idea of what
# encryption really is.
example_message = 'Hello World'
example_key = 11
enc = encrypt(example_message, example_key)
print(enc)
dec = encrypt(enc, 11)
print(dec)


