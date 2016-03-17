import binascii
import numpy
import math
import re

def hex_string_to_array(string):
    return numpy.array(bytearray(binascii.unhexlify(string)))

def array_to_hex_string(array):
    return binascii.hexlify(bytearray(array))



class NgramScore(object):
    def __init__(self, ngram_file):
        """
        Example of the 4-grams file structure
        TION 13168375
        NTHE 11234972
        THER 10218035
        THAT 8980536
        OFTH 8132597
        """

        self.ngrams = {}

        
        with open(ngram_file) as fd:
            for line in fd:
                key, count = line.split(' ')
                self.ngrams[key] = int(count)
                

        self.L = len(key)
        self.N = sum(self.ngrams.itervalues())

        for key in self.ngrams:
            self.ngrams[key] = math.log10(float(self.ngrams[key])/self.N)
            
        self.floor = math.log10(0.01/self.N)

    def score(self, text):
        score = 0

        text = text.upper()
        
        for i in xrange(len(text)-self.L+1):
            key = text[i:i+self.L]

            if key in self.ngrams:
                score += self.ngrams[key]
            else:
                score += self.floor
                
        return score
    
