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





# This is English language scoring code
# requires A LOT of re-factoring and optimization
# I'm 99.9% it can be done simpler

class LanguageModel(object):
    def __init__(self):
        self.__ngrams_by_length = {}

    def add_ngram_stat(self, n, ngrams):
        self.__ngrams_by_length[n] = ngrams


    def ngrams_by_len(self, n):
        return self.__ngrams_by_length[n]



class NgramScore(object):
    def __init__(self, pickled_model):
        fd = open(pickled_model, 'rb')
        self.model = pickle.load(fd)
        fd.close()

    
    def score(self, text):
        score = 0

        if not text:
            return 0
        
        # Our n-grams are lowercase
        text = text.lower()

        # Split into words
        words = re.split(r'\s+', text)

        
        for word in words:
            if not word:
                continue

            n = len(word)

            if n < 5:
                ngrams = self.model.ngrams_by_len(n)
                floor = math.log10(0.01/len(ngrams.keys()))
                
                if word in ngrams:
                    score += ngrams[word]
                else:
                    score += floor

            else:
                
                ngrams = self.model.ngrams_by_len(4)
                floor = math.log10(0.01/len(ngrams.keys()))
                
                for i in xrange(len(word) - 3):
                    key = word[i:i+4]
                
                    if key in ngrams:
                        score += ngrams[key]
                    else:
                        score += floor

	return score
