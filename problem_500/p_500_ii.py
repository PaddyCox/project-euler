"""">>>500_iii: Create algorithm to solve for ceiling of dDdn rather than iterating through 500500"""

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


def bisect_find(n):
    l = len(primes_i)
    lower_bound = 0
    upper_bound = l
    range_b = l

    while range_b > 1:
        mid_p = (lower_bound + upper_bound) //2
        if primes_i[mid_p] < n:
            lower_bound = mid_p
        else:
            upper_bound = mid_p
        range_b = upper_bound - lower_bound
    print('bisect_find:', n, primes_i[lower_bound], lower_bound, mid_p, upper_bound)
    return lower_bound


check_p = rwh_primes(5*10**7)

num_primes = len(check_p)

print('len check_p', len(check_p))

primes_i = [check_p[i] for i in range(0, num_primes)]

x_i = len(primes_i) * [0]

x_options = [0, 1, 3, 7, 15, 31, 63, 127]

def p_finder(p_x, x_0, x_1, y_0=0, y_1=1):
    c = ((x_0 + 1) * (p_x**(x_1 - x_0))) / (x_1 + 1)
    p_y = (((y_0 + 1)* c)/(y_1 + 1))**(1/(y_1 - y_0))
    print('p_finder:', p_x, x_0, x_1, y_0, y_1, p_y)
    return p_y

def p_finder_ii(inverse_gradient, y_0=0, y_1=1):
    p = (inverse_gradient*(y_0 + 1)/(y_1 + 1))**(1/(y_1 - y_0))
    return p

def x_power_allocate(exponent_2):
    x_i[0] = exponent_2
    globals()
    p_range = [1]
    two_low = (exponent_2 + 1)//2 - 1
    for i in range(x_options.index(two_low), 0, -1):
        p_i_int = (p_finder(2, two_low, exponent_2, x_options[i - 1], x_options[i]))
        p_i_index = bisect_find(p_i_int) + 1
        p_range.append(p_i_index)
        r_l, r_u = p_range[x_options.index(two_low) - i], p_i_index
        len_range = r_u - r_l
        print('r_l, r_u:', r_l, r_u, len_range, x_options[i])
        x_i[r_l: r_u] = len_range * [x_options[i]]
    print('p_range:', p_range)

x_power_allocate(63)
print('len_xi', len(x_i))

dDdn = [(2 * (x_i[i] + 1) - 1)/(primes_i[i]**x_i[i]) for i in range(0, len(primes_i))]

start_count = sum(x_i)
temp_c = 0
count = 0

print('start_count:', start_count)

while count < 0:
    dDdn_current = max(dDdn)
    i = dDdn.index(dDdn_current)
    p_i = primes_i[i]
    x_0 = x_i[i]
    try:
        x_1 = x_options[x_options.index(x_0) + 1]
    except IndexError:
        print(x_0, p_i, count)
        break
    dDdn_new = (x_1 + 1)/((x_0 + 1) * (p_i**(x_1 - x_0)))
    x_i[i], dDdn[i] = x_1, dDdn_new
    count += (x_1 - x_0)
    temp_c += (x_1 - x_0)
    if temp_c > 50:
        print(count, p_i, dDdn_current, dDdn_new, x_1, dDdn[500000])
        temp_c = 0

for j in range(500):
    print(primes_i[j], x_i[j], dDdn[j])

