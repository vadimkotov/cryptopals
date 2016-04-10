"""
Single-byte XOR cipher
The hex encoded string:

1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
... has been XOR'd against a single character. Find the key, decrypt the message.

You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

"""


# Intersting writeup on scoring english language
# http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/#a-python-implementation
# the implementation of NgramScore is heavily based on it
# it is based on quad-grams just for the heck of it, you can speed it up by using tri- or bi-grams
# also you can optimize it if you pre-process the file and calcuated logarithmic probabilities beforehand



from core import *

ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

ngram_collection = load_ngram_collection('core/eng_wnp.pickle')
ngrams = ngram_collection[3]



ciphertext = hex_string_to_array(ciphertext)

cleartext = ''

max_score = None
key = 0

for i in xrange(256): 
   
    potential_cleartext = str(bytearray((ciphertext ^ i)))

    score = lang_score(potential_cleartext, ngrams)
    
    if score == 0:
        continue

    if max_score == None:
        max_score = score
    elif score > max_score:
        max_score = score
        cleartext = potential_cleartext
        key = i


print 'Cleartext:', cleartext
print 'Key:', hex(key)
print 'Fitness:', max_score
