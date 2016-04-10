
def is_ecb_mode(text, block_size = 16):

    for i in xrange(0, len(text), block_size):
        for j in xrange(i+block_size, len(text), block_size):
            if text[i:i+block_size] == text[j:j+block_size]:
                return (i, j)
            

