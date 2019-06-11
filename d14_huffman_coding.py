from collections import Counter

def find_min(freq):
    output = min(freq, key=lambda i: i[0])
    freq.remove(output)

    return output

def print_freq(tree, prefix=''):
    if isinstance(tree,tuple):
        print_freq(tree[0], prefix + '0')   # add code
        print_freq(tree[1], prefix + '1')
    else:
        print(tree, prefix)

def huffman_coding(text):
    freq = [(i, x) for x, i in Counter(text).items()]

    while len(freq) > 1:    # till last one
        mI1, mX1 = find_min(freq)
        mI2, mX2 = find_min(freq)
        freq.append((mI1 + mI2, (mX1, mX2)))
    
    print_freq(freq.pop()[1])
    # print(freq)
    # return freq

huffman_coding('huffman. coding. practice huffman')
