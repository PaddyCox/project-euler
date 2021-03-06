import time
import numpy as np
from array import array



t_0 = time.time()

sums_nk = [0, 1, 2, 3]
n_k = [array('i', [0]), array('i', [0, 1]), array('i', [0, 1, 1]), array('i', [0, 1, 1, 1])]

for n in range(4, 10000):
    list_n_k = [0]
    for k in range(1, n//2 + 1):
        list_n_k.append(int(str(n_k[n-1][k-1] + n_k[n-k][k])[-6::]))
    for k in range(n//2 + 1, n + 1):
        #print(n, k, n_k)
        #print(n_k[n-1][k-1])
        list_n_k.append(int(str(n_k[n-1][k-1])[-6::]))
    n_k.append(array('i', list_n_k))
    sum_nk = sum(list_n_k)
    sums_nk.append(sum_nk)
    # print(n, sum_nk)
    if sum_nk % 100 == 0:
        print(n, sum_nk)
    if sum_nk % 10**6 == 0:
        print("Answer is:", sum_nk, n)
        break
    #print(n, sum_nk)


print(time.time() - t_0)