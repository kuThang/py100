import numpy as np
from itertools import zip_longest
def add(x, y):
    z, carry = [], 0
    for xi, yi in zip_longest(x, y, fillvalue=0):
        add_i = xi + yi + carry
        carry = add_i // 10
        z.append(add_i % 10)
    if carry :
        z.append(carry)
    return z

def sub(x, y):
    z, carry = [], 0
    for xi, yi in zip_longest(x, y, fillvalue=0):
        add_i = xi - yi + carry
        carry = add_i // 10
        z.append(add_i % 10)
    if carry :
        z.append(carry)
    return z

def karatsuba(x, y):
    while len(x) != len(y):
        if len(x) < len(y):
            x.append(0)
        else : 
            y.append(0)
    n = len(x)
    n_2 = (n+1) >> 1
    if n == 1:
        sum_2 = add([x[0] * y[0]], [])
        return sum_2
        
    x1 = x[n_2:]
    x0 = x[:n_2]
    y1 = y[n_2:]
    y0 = y[:n_2]

    z0 = karatsuba(x0, y0)
    z2 = karatsuba(x1, y1)
    z1 = karatsuba(add(x0, x1), add(y0, y1))
    z1 = sub(sub(z1, z0), z2)

    z = add(z0, [0] * (n_2 << 1) + z2)
    z = add(z, [0] * n_2 + z1)

    return z

# x = '789456123'
# y = '898989898989'

x = '11'
y = '1111'

x_arr = list(map(int, reversed(x)))
y_arr = list(map(int, reversed(y)))

print(x_arr)
print(y_arr)

mul = karatsuba(x_arr, y_arr)
print(mul)
print(''.join(map(str, reversed(mul))))
