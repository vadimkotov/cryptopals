from core import *

def is_ecb_mode(text, block_size = 16):
    for i in xrange(0, len(text), block_size):
        for j in xrange(i+block_size, len(text), block_size):
            if text[i:i+block_size] == text[j:j+block_size]:
                return (i, j)
            
def pad_pkcs7(text, block_size = 16):    
    if len(text) % block_size == 0:
        return text

    pad_size = (len(text) / block_size + 1) * block_size - len(text)
    return text + chr(pad_size) * pad_size



def cbc_decrypt(text, cipher, IV):
    block_size = len(IV)

    prev_ct_block = string_to_array(IV)

    plaintext = ''
    
    for i in xrange(0, len(text), block_size):

        ct_block = text[i:i+block_size]
        m_block = string_to_array(cipher.decrypt(ct_block))

        
        pt_block = prev_ct_block ^ m_block

        prev_ct_block = string_to_array(ct_block)
        plaintext += str(bytearray(pt_block))

    return plaintext[:-ord(plaintext[-1])]
