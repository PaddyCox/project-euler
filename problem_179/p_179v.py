import time
from operator import add

t_0 = time.time()

def factors_sieve(n):
    sieve = [1] + [2] * (n - 1)

    for i in range(2, int(n**0.5) + 1):
        print(i, sieve[i**2::i], [1]*((n - i**2 + 1)//i))
        sieve[i**2::i] += [1] * ((n - i**2 + 1)//i)
        print(sieve)
    return sieve


def factors_sieve_ii(n):
    sieve_ii = [0, 1] + [2] * (n - 1)

    for i in range(2, int(n**0.5) + 1):
        sieve_ii_i = [0] * (n + 1)
        sieve_ii_i[i**2] = 1
        sieve_ii_i[i**2 + i: n + 2: i] = [2] * ((n - i**2 - i)//i + 1)
        sieve_ii += sieve_ii_i
    return sieve_ii

n_test = 100000

solution_ii = factors_sieve_ii(n_test)

total = 0

for i in range(2, n_test + 1):
    if solution_ii[i] == solution_ii[i-1]:
        #print(i, i-1)
        total += 1

print(total)

print(time.time() - t_0)
#print(factors_sieve(20))