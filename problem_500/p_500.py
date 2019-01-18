"""Contains dict operation testing, clean solution continued in p_500_ii"""

from useful_functions import find_p_factors, rwh_primes
import numpy as np
import timeit

def num_divisors(n):
    """Return a list of all integer divisors of n"""
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors += {i, n //i}
    return divisors

largest_divisor = 0

def num_divisors_ii(n):
    """Return number of divisors of integer 'n' based on prime of factors of n"""
    set_pf = set(n)
    n_og = 2**(len(set_pf))
    n_div = n_og
    for pf in set_pf:
        x = n.count(pf)
        n_div += n_div//2 * (x - 1)
    return n_div

def num_divisors_iii(n):
    """Return number of divisors of integer 'n' based on prime of factors of n"""
    set_pf = set(n)
    n_div = 1
    for pf in set_pf:
        x = n.count(pf)
        n_div *= (1 + x)
    return n_div

def np_argmin(a):
    return np.argmin(a)

for x in range(10000):
    n_div = len(num_divisors(x))
    if n_div > largest_divisor:
        print(x, n_div, num_divisors_ii(find_p_factors(x)), num_divisors_iii(find_p_factors(x)))
        largest_divisor = n_div

check_p = rwh_primes(75 * 10**5)

dDdn_primes = {check_p[i]: 2 / check_p[i] for i in range(0, 500500)}


x_options = [1, 3, 7, 15, 31, 63]

count = 0

"""while count < 500500:
    dD_dn_index = dD_dn.index(min(dD_dn))
    x_0 = dict_primes"""

def min_index_i(a):
    return min(range(len(a)), key=a.__getitem__)

def min_index_ii(values):
    return min(range(len(values)), key=values.__getitem__)

def paddy_min(values):
    return values.index(min(values))

def dict_min(values):
    return (min(values.items(), key=lambda x: x[1]))

def dict_min_ii(values):
    return (min(values, key=values.get))

def dict_min_iii(values):
    return (min(values.items(), key=lambda x: x[1][1]))

test_values = [2, 4, 6, 9, 16, 1, 28, 10]

test_values_ii = {i:test_values[i] for i in range(8)}

test_values_iii = {i:(test_values[i]*(i+1), test_values[i]) for i in range(8)}

print('dict_test', (test_values_ii), test_values_ii.items(), test_values_ii.keys(), test_values_ii.values())

print('dict_test', dict_min(test_values_ii))

print('dict_test_ii', dict_min_ii(test_values_ii))

print('dict_test_iii', dict_min_iii(test_values_iii), test_values_iii)

print('dict_test_iii', test_values_iii.items())

print(min_index_i(test_values), min_index_ii(test_values), min(test_values_ii))

print(timeit.timeit('min_index_i(test_values)', globals=globals()))

print(timeit.timeit('min_index_ii(test_values)', globals=globals()))

print(timeit.timeit('paddy_min(test_values)', globals=globals()))

print(timeit.timeit('dict_min(test_values_ii)', globals=globals()))

print(timeit.timeit('dict_min_ii(test_values_ii)', globals=globals()))

print(timeit.timeit('dict_min_iii(test_values_iii)', globals=globals()))