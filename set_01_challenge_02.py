"""
Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

If your function works properly, then when you feed it the string:

1c0111001f010100061a024b53535009181c
... after hex decoding, and when XOR'd against:

686974207468652062756c6c277320657965
... should produce:

746865206b696420646f6e277420706c6179
"""


from core import *

src_string = '1c0111001f010100061a024b53535009181c'
xor_string = '686974207468652062756c6c277320657965'
expected_result = '746865206b696420646f6e277420706c6179'

answer = xor(string_to_array(src_string), string_to_array(xor_string))

answer = array_to_string(answer)

print answer

if answer == expected_result:
    print 'Correct!'
