import binascii

# Given encrypted message (hex encoded)
hex_message = (
    "1c1c01041963730f31352a3a386e24356b3d32392b6f6b0d323c22243f6373"
    "1a0d0c302d3b2b1a292a3a38282c2f222d2a112d282c31202d2d2e24352e60"
)

# Convert hex to bytes
ciphertext = binascii.unhexlify(hex_message)

# Known plaintext at the beginning of the message
known_plaintext = b"ORDER:"

# Determine the key by XORing the ciphertext with the known plaintext
key = bytes([ciphertext[i] ^ known_plaintext[i] for i in range(len(known_plaintext))])

# Apply the repeating-key XOR decryption
decrypted_message = bytes([ciphertext[i] ^ key[i % len(key)] for i in range(len(ciphertext))])

# Convert decrypted bytes to a string
decrypted_message.decode(errors="ignore")
