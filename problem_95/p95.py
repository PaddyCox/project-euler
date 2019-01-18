# Two aspects to n: nominal value, sum_of_factors
# Possible outcomes from start chain n
# n + i > 10**6 - Not an acceptable chain
# n + i = 1 - Not a chain
# n + i = n - Chain

from collections import defaultdict as ddict
from useful_functions import rwh_primes

primes = rwh_primes(10**6)


def p_factors(n):
    n_temp = n
    p_max = int(n_temp**0.5)
    p_fact_n = []
    p = iter(primes)
    p_i = next(p)
    while n_temp > 1:
        if n_temp % p_i == 0:
            p_fact_n.append(p_i)
            n_temp //= p_i
            p_max = int(n_temp**0.5)
        else:
            p_i = next(p)
            if p_i > p_max:
                p_fact_n.append(n_temp)
                return p_fact_n
    return p_fact_n

def all_factors(n):
    n_temp = n
    p_max = int(n_temp**0.5)
    p_fact_n = {1}
    p = iter(primes)
    p_i = next(p)
    while n_temp > 1:
        if n_temp % p_i == 0:
            p_fact_n = p_fact_n | {p_i * i for i in p_fact_n}
            n_temp //= p_i
        else:
            if p_i >= min(p_max, n_temp):
                p_fact_n = p_fact_n | {n_temp * i for i in p_fact_n}
                return sorted(list(p_fact_n))
            p_i = next(p)
    return sorted(list(p_fact_n))

def p_factors_d(n):
    n_temp = n
    p_max = int(n_temp**0.5)
    p_fact_n = ddict(int)
    p = iter(primes)
    p_i = next(p)
    while n_temp > 1:
        if n_temp % p_i == 0:
            p_fact_n[p_i] += 1
            n_temp //= p_i
            p_max = int(n_temp**0.5)
        else:
            p_i = next(p)
            print(p_i, n_temp)
            if p_i > p_max:
                p_fact_n[n_temp] += 1
                return p_fact_n
    return p_fact_n

for j in range(2, 50):
    print(p_factors(j))
    print('AF', j, all_factors(j))


default_s = ddict(int)


def loop(n):
    current_loop = [n]
    n_new = sum(all_factors(n)) - n
    while n_new not in current_loop:
        current_loop.append(n_new)
        n_new = -n_new + sum(all_factors(n_new))
        if n_new in default_s:
            v_n = default_s[n_new]
            for i in current_loop:
                default_s[i] = v_n
                return
        if n_new > 10**6:
            for i in current_loop:
                default_s[i] = 9999999
                return
    for i in current_loop:
        default_s[i] = 0
    current_loop = current_loop[current_loop.index(n_new):]
    print('Loop size, min member:', len(set(current_loop)), min(current_loop))

print(all_factors(5))


for i in range(1, 10**6 + 1):
    if i in default_s:
        pass
    else:
        loop(i)


"""def recurs

def sum_divisors(n):
    p_n = p_factors(n)
    s_p_n = set(p_n)"""


# def amicable_chain(x):
