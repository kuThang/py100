# how to find pi with random number generator

import numpy as np

def pi(sample):
    batch = 1000
    n = sample // batch
    total_less_than_1 = 0
    for i in range(n):
        rand_num = np.random.rand(batch, 2)
        square_total = (rand_num * rand_num).sum(axis=1)
        total_less_than_1 += (square_total <= 1).sum()
    
    print('P(x2 + y2 <= 1) = ', total_less_than_1 / sample)
    print('approx pi is ', 4 *  total_less_than_1 / sample)
    return 4 *  total_less_than_1 / n
    
pi(10**8)