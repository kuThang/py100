import numpy as np
import math
import time
def find_prime(n):
    flags = np.ones(n, dtype=np.int8)
    flags[:2] = 0
    max_num = math.floor(math.sqrt(n))
    for i in range(2, max_num):
        if flags[i]:
            flags[ [i + j for j in range(i, n - i, i)] ] = 0

    return [i for i in range(n) if flags[i] == 1]



s = time.time()
a = find_prime(100000)
e = time.time()
print('time = ', e - s)
print('found ', len(a), ' number')
# print(a)
