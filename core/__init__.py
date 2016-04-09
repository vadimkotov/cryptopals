import binascii
import numpy
import math
import re
import string
import pickle

def hex_string_to_array(string):
    return numpy.array(bytearray(binascii.unhexlify(string)))

def array_to_hex_string(array):
    return binascii.hexlify(bytearray(array))


def load_ngram_collection(filename):
    return pickle.load(open(filename, 'rb'))


def eng_score(text, ngrams):
    
    if not text:
        return 0
    
        
    # Our n-grams are lowercase
    text = text.lower()

    score = 0

    # What's n
    n = len(ngrams.keys()[0])
    
    # Just a super small value for non-existsnt ngrams (because it can't be 0)
    floor = math.log10(0.01/len(ngrams.keys()))


    for i in xrange(len(text) - n + 1):
        
        key = text[i:i+n]

        if key in ngrams:
            score += ngrams[key]
        else:
            score += floor
            
    return score

