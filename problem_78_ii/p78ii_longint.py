"""Let p(n) represent the number of different ways in which n coins can be separated into piles.
 For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.
 Find the least value of n for which p(n) is divisible by one million."""

# Euler Pentagonal Number Theorem

import time
import numpy as np

t_0 = time.time()

p_s = np.array([0] * 15000, dtype='int64')

for k in range(1, 100):
    k_pos = int((-1)**(k) * ((-k) * (3*k - 1))//2)
    k_neg = int((-1)**(-k) * ((k) * (3*-k - 1))//2)
    p_s[abs(k_pos)], p_s[abs(k_neg)] = (-1)**(k + 1), (-1)**(k+1)

print(p_s[1:100])

partitions_n = np.array([1])

def partition_recur(n):
    global partitions_n
    for i in range(1, n + 1):
        #print(i, partitions_n, p_s[i:0:-1])
        p_n = np.dot(p_s[i:0:-1], partitions_n)
        if p_n > 10**18:
            print(i)
            break
        """if p_n < 0:
            test_pn = np.multiply(p_s[i:0:-1], partitions_n)
            trim_pn = np.trim_zeros(test_pn)
            print(p_n, i, test_pn, trim_pn, sum(test_pn))
            break"""
        #print('p_n:', p_n)
        #print(p_n)
        if p_n % 10**2 == 0:
            print(i, p_n)
        partitions_n = np.append(partitions_n, p_n)


partition_recur(500)

print(partitions_n)

print(time.time() - t_0)
