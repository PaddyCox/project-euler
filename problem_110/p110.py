import copy

import time

from useful_functions import find_p_factors_ii as fact_find
import itertools
"""def recursive_p_fact(z, seed):
    count = 0
    seed_copy = seed
    max = z
    p_fact = find_p_factors_ii(z)
    set_p_fact = set(p_fact)
    for f in set_p_fact:"""

def brute_recursive(z, max_n, factors):
    """Return all integers < z that divide z**2"""
    if z > max_n:
        return []
    integers_z = [z]

    for f in factors:
        remaining_pf = copy.copy(factors)
        remaining_pf.remove(f)
        z_new = z * f
        integers_z += brute_recursive(z_new, max_n, remaining_pf)

    return integers_z

def brute_recursive_ii(z, max_n, factors):
    """Return all integers < z that divide z**2"""
    if z > max_n:
        return []
    integers_z = [z]

    n_factors = len(factors)
    for i in range(0, len(factors)):
        copy_factors = copy.copy(factors)
        remaining_pf = copy_factors[i+1:]
        z_new = z * copy_factors[i]
        integers_z += brute_recursive(z_new, max_n, remaining_pf)

    return integers_z

def brute_num_n(n):
    total = 0
    for x in range(n + 1, n * 2 + 1):
        if (n * x) % (x - n) == 0:
            total += 1
    return total

x = 2 * 2

count_0 = 0
count_2 = 0

for y in range(1, x + 1):
    if x**2 % y == 0:
        count_0 += 1
        if y % 2 == 0:
            count_2 += 1
print(count_0, count_2)

t_0 = time.time()

test_solution = brute_recursive(1, 2*3*5*7*11*13, [2, 3, 5, 7, 11, 13]*2)

t_1 = time.time()

test_solution_ii = brute_recursive_ii(1, 2*3*5*7*11*13, [2, 3, 5, 7, 11, 13]*2)

t_2 = time.time()

test_solution_iii = brute_num_n(2*3*5*7*11*13)

t_3 = time.time()

print(len(set(test_solution)))
print(len(set(test_solution_ii)))
print((test_solution_iii))

print(sorted(set(test_solution)))
print(sorted(set(test_solution_ii)))
print((set(test_solution_ii))-set(test_solution))

print(t_1 - t_0, t_2 - t_1, t_3 - t_2)