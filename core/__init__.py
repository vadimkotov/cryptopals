import binascii
import numpy
import math
import re
import string
import pickle

# Helper function
def string_to_array(string):
    return numpy.array(bytearray(string))


def hex_string_to_array(string):
    #return numpy.array(bytearray(binascii.unhexlify(string)))
    return string_to_array(binascii.unhexlify(string))


def array_to_hex_string(array):
    return binascii.hexlify(bytearray(array))

def hamming_distance(x, y):
    if len(x) != len(y):
        return -1

    xored = x ^ y
    return sum(numpy.unpackbits(xored))
    

# Basic XOR crypto
def repeating_key_xor(data, key):

    xored = []
    
    for i in xrange(len(data)):
        xored.append(data[i] ^ key[i%len(key)]) 
    return xored



# Language model and text scoring


def load_ngram_collection(filename):
    return pickle.load(open(filename, 'rb'))

def lang_score(text, ngrams):
    
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

