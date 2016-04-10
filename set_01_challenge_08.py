"""
Detect AES in ECB mode
In this file (http://cryptopals.com/static/challenge-data/8.txt) are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.
"""

import binascii
from core import *
from core import block_crypto

fd = open('files/8.txt', 'rb')
lines = fd.read().split('\n')
fd.close()




for i in xrange(len(lines)):
    ciphertext = binascii.unhexlify(lines[i])

    indices = block_crypto.is_ecb_mode(ciphertext)

    if indices != None:
        print 'Line #', i
        print
        print lines[i]
        print
        print 'Blocks with resumably same cleartext:'
        print
        x, y = indices
        print '(Offset %d) %s' % (x, lines[i][x*2:x*2+32])
        print '(Offset %d) %s' % (y, lines[i][y*2:y*2+32])
        print
        print





