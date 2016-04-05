"""
One of the 60-character strings in this file* has been encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)


* http://cryptopals.com/static/challenge-data/4.txt
  or in  the 'files' folder
"""

from core import *



ngram_score = NgramScore('core/model.pickle')

cleartext = ''
max_score = None

# scores = []


for line in file('files/4.txt'):
    ciphertext = hex_string_to_array(line.strip())

    
    
    for i in xrange(256):
        potential_cleartext = str(bytearray((ciphertext ^ i)))

        score = ngram_score.score(potential_cleartext)

        
        if score == 0:
            continue
        #print score
        if not max_score:
            max_score = score
        elif score > max_score:
            max_score = score
            cleartext = potential_cleartext

    #scores.append((max_score, cleartext))
 


#scores = sorted(scores, key=lambda x: x[0])
    

print cleartext, max_score
