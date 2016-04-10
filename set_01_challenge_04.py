"""
One of the 60-character strings in this file* has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)


* http://cryptopals.com/static/challenge-data/4.txt
  or in  the 'files' folder
"""

from core import *




ngram_collection = load_ngram_collection('core/eng_wnp.pickle')
ngrams = ngram_collection[3]

cleartext = ''
max_score = None



cnt = 0
for line in file('files/4.txt'):
    cnt += 1
    
    ciphertext = hex_string_to_array(line.strip())

        
    for i in xrange(256):
        potential_cleartext = str(bytearray((ciphertext ^ i)))

        score = lang_score(potential_cleartext, ngrams)

        if score == 0:
            continue
        #print score
        if not max_score:
            max_score = score
        elif score > max_score:
            max_score = score
            cleartext = potential_cleartext


    
print 'Cleartext:', cleartext
print 'Fitness:', max_score
print 'Line #:', cnt
