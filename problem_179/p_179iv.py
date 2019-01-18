import time
import numpy as np

t_0 = time.time()

def factors_sieve_ii(n):
    sieve_ii = np.array([0, 1] + [2] * (n - 1))

    for i in range(2, int(n**0.5) + 1):
        sieve_0 = np.zeros((n+1,), dtype=int)
        sieve_0[i**2] = 1
        sieve_0[i**2 + i: n + 1: i] = [2]
        sieve_ii += sieve_0
    return sieve_ii

n_test = 1000000

solution_ii = factors_sieve_ii(n_test)

total = 0

for i in range(2, n_test + 1):
    if solution_ii[i] == solution_ii[i-1]:
        #print(i, i-1)
        total += 1

print(total)

print(time.time() - t_0)
#print(factors_sieve(20))