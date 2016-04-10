"""
The Base64-encoded content in this file (http://cryptopals.com/static/challenge-data/7.txt) has been encrypted via AES-128 in ECB mode under the key

"YELLOW SUBMARINE".
(case-sensitive, without the quotes; exactly 16 characters; I like "YELLOW SUBMARINE" because it's exactly 16 bytes long, and now you do too).

Decrypt it. You know the key, after all.

Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher.
"""

# We'll be using PyCrypto: https://github.com/dlitz/pycrypto
# I remember Dan Boneh recommended it for solving
# assignments in his coursera class Cryptography I
# so if it's good for him it's good for us.

import base64
from Crypto.Cipher import AES


key = "YELLOW SUBMARINE"

cipher = AES.new(key, AES.MODE_ECB)


fd = open('files/7.txt')
ciphertext = base64.b64decode(fd.read())
fd.close()

print cipher.decrypt(ciphertext)
