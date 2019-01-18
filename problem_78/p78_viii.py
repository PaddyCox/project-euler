import time
import numpy as np
from array import array


t_0 = time.time()

sums_nk = [0, 1, 2, 3]
n_k = [[0], [0, 1], [0, 1, 1], [0, 1, 1, 1]]

# Partition number theory
# Elliptic modular functions
# Euler pentagonal number theorem
# Generator function



t_0 = time.time()

# Make as a generator function

partition_dict = {'0_0' : 0, '1_0': 0, '1_1': 1, '2_0': 0, '2_1': 1, '2_2': 1}

for n in range(3, 2000):
    sum_n_k = 0
    partition_dict.update({str(n) + '_' + str(0): 0})
    for k in range(1, n//2 + 1):
        i_n_k = partition_dict[(str(n-1) + '_' + str(k-1))] + partition_dict[(str(n-k) + '_' + str(k))]
        partition_dict.update({str(n) + '_' + str(k): i_n_k})
        sum_n_k += i_n_k
    for k in range(n//2 + 1, n + 1):
        i_n_k = partition_dict[str(n-1) + '_' + str(k-1)]
        partition_dict.update({str(n) + '_' + str(k): i_n_k})
        sum_n_k += i_n_k
    sums_nk.append(sum_n_k)
    # print(n, sum_nk)
    #print(partition_dict)
    if sum_n_k % 100 == 0:
        print(n, sum_n_k)
    if sum_n_k % 10**6 == 0:
        print("Answer is:", sum_n_k, n)
        break
    #print(n, sum_nk)


print(time.time() - t_0)

