"""
This script generates a collection of ngram
propabilities for n = 1 to 4
"""
import sys
import re
import string
import math
import pickle

NMAX = 4



def read_file(path):
    fd = open(path)
    data = fd.read()
    fd.close()
    return data


def normalize(text):
    # Remove whitespaces and line breaks
    text = re.sub(r'\s+|[\n\r]', ' ', text)

    # Remove non-printable chharacters
    text = ''.join(c for c in text if c in string.printable)

    # Make lowercase
    text = text.lower()
    return text

def slice_into_ngrams(n, text):
    return [text[i:i+n] for i in xrange(len(text)-n+1)]


def calc_ngram_probabilities(ngrams):
    ngram_prob = {}
    
    for ngram in ngrams:
        if ngram not in ngram_prob:
            ngram_prob[ngram] = 0
            
        ngram_prob[ngram] += 1

    total = len(ngram_prob)
        
    for ngram in ngram_prob:
        ngram_prob[ngram] = math.log10(float(ngram_prob[ngram])/total)
        
    return ngram_prob




def main():

    if len(sys.argv) != 3:
        exit('Usage: %s <input file> <output file>' % sys.argv[0])
    
    text = read_file(sys.argv[1])
    text = normalize(text)

    ngram_collection = {}
    
    for i in xrange(1, NMAX+1):
        ngrams = slice_into_ngrams(i, text)
        ngram_prob = calc_ngram_probabilities(ngrams)
        ngram_collection[i] = ngram_prob

    pickle.dump(ngram_collection, open(sys.argv[2], 'wb'))
        
if __name__ == '__main__':
    main()


