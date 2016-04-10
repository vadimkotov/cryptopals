"""
There's a file (http://cryptopals.com/static/challenge-data/6.txt) here. It's been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

1. Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

2. Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:

this is a test

and

wokka wokka!!!

is 37. Make sure your code agrees before you proceed.

3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.

4. The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.

5. Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.

6. Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.

7. Solve each block as if it was single-character XOR. You already have code to do this.

8. For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.

.This code is going to turn out to be surprisingly useful later on. Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing. But more people "know how" to break it than can actually break it, and a similar technique breaks something much more important.
"""
import base64
from core import *

"""
Testing hamming distance
x = string_to_array("this is a test")
y = string_to_array("wokka wokka!!!")
print hamming_distance(x, y)
"""


def get_normalized_edit_distance(key_size, data):
    n = 8
    d = 0
    
    for i in range(0, key_size*n*2, key_size*2):
        key1 = string_to_array(data[i:i+key_size])
        key2 = string_to_array(data[i+key_size:i+2*key_size])
        d += (float(hamming_distance(key1, key2))/key_size)

    return d/n
    


def break_single_xor(block, unigrams):

    max_score = None
    key = 0

    block = string_to_array(block)
    
    for i in xrange(256):
        potential_cleartext = str(bytearray(block ^ i))

        score = lang_score(potential_cleartext, unigrams)

        if score == 0:
            continue

        if (max_score == None) or (score > max_score):
            max_score = score
            key = i
            ct = potential_cleartext

    return key


fd = open('files/6.txt')
data = fd.read()
fd.close()


data = base64.b64decode(data)

ngram_collection = load_ngram_collection('core/eng_wnp.pickle')
unigrams = ngram_collection[1]


distances = []

for key_size in xrange(2, 41):
    normalized_edit_distance = get_normalized_edit_distance(key_size, data)
    distances.append((key_size, normalized_edit_distance))


n_keys_to_try = 1


for key_size, _ in sorted(distances, key=lambda x: x[1])[:n_keys_to_try]:
    print 'Checking key size', key_size

    data_blocks = [data[i:i+key_size] for i in xrange(0, len(data)-key_size, key_size)]


    key = []
    
    for i in xrange(key_size):
        single_xor_block = ''.join([block[i] for block in data_blocks])

        
        key_byte = break_single_xor(single_xor_block, unigrams)
        key.append(key_byte)

    print
    print 'Key =', bytearray(key)
    print 'Cleartext:'
    print bytearray(repeating_key_xor(bytearray(data), bytearray(key)))
    print
