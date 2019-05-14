def getLastBit(input):
    a = input >> 1
    b = a << 1
    sub = input - b
    
    return sub

print(getLastBit(0b1111))

def count_of_1_bits(input):
    n = 0
    while input:
        input &= input - 1
        n += 1
    return n

def count_of_0_bits(input):
    return input.bit_length() - count_of_1_bits(input)

print(count_of_1_bits(0b1111111111000000000000000)) # 10
print(count_of_0_bits(0b1111111111000000000000000)) # 15