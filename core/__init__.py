import binascii
import numpy

def string_to_array(string):
    return numpy.array(bytearray(binascii.unhexlify(string)))

def xor(x,y):
    return x^y

def array_to_string(array):
    return binascii.hexlify(bytearray(array))
