import itertools
import math
from useful_functions import rwh_primes
import timeit
import time


t_0 = time.time()

potential_primes = rwh_primes(987654321)

t_1 = time.time()

print(t_1 - t_0)

set_p_p = set(potential_primes)


"""
perm_3 = itertools.permutations('1234')

print(len(list(perm_3)))

print(math.factorial(9) * 2**8)

print(type(potential_primes))

test_numbers = [int(x+y) for x, y in itertools.combinations_with_replacement('123456789', 2)]

print(test_numbers)


print(timeit.timeit('[n in potential_primes for n in test_numbers]', globals=globals(), number=1000))

print(timeit.timeit('[n in set_p_p for n in test_numbers]', globals=globals(), number=1000))

Searching for instance in set ~25 times faster than list"""

def recursive_pandigital_prime_sets(d, max_d, previous_p):
    solutions = 0
    num_digits = len(d)
    if num_digits == 0:
        return 1
    for l in range(max_d, 0, -1):
        for p in itertools.permutations(d, l):
            p_int = int(''.join(p))
            if p_int in set_p_p and p_int < previous_p:
                remaining_digits = d - set(p)
                solutions += recursive_pandigital_prime_sets(remaining_digits, min(len(remaining_digits), l), p_int)
    return solutions

print(recursive_pandigital_prime_sets(set([str(i) for i in range(1, 10)]), 9, 999999999))

t_2 = time.time()

print(t_2 - t_0)