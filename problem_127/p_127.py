import math
import operator
import itertools
from functools import reduce
from useful_functions import find_p_factors_ii
from useful_functions import rwh_primes
print(math.gcd(10, 55))

prime_set = rwh_primes(1000)

def product(i):
    return reduce(operator.mul, i, 1)


def rad(n):
    pf_n = set(find_p_factors_ii(n))
    return product(pf_n), pf_n

for c in range(2, 1000):
    temp_primes = prime_set[:]
    s_c, pf_c = rad(c)
    for p in pf_c:
        temp_primes.remove(p)
    max_val_ab = c / (s_c)
    max_prod_ab = max_val_ab // temp_primes[0]
    primes_ab = []
    i = 0
    while temp_primes[i] < max_prod_ab:
        primes_ab.append(temp_primes[i])
        i += 1
    ab_prime_sets = []
    for j in range(2, len(primes_ab) + 1):
        ab_prime_sets += [p_s for p_s in itertools.combinations(primes_ab, j)]

    for combo in ab_prime_sets:
        if product(combo) > max_val_ab:
            print(combo)

