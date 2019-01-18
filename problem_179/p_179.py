import collections
import itertools
import useful_functions
import time

def num_p_factors(list_p):
    """
    Returns frequency of unique integers in list_p
    :param list_p:
    :return: sorted list of occurrences
    """
    d_1 = {}

    for p in list_p:
        if p in d_1:
            d_1[p] += 1
        else:
            d_1[p] = 1

    l_r = sorted(d_1.values())

    return l_r

primes_1 = useful_functions.rwh_primes(1000000)

t_0 = time.time()

list_n =[]
count = 0

for n in range(2, 10000):
    n_i = 2
    max_i = int(n**0.5)
    for i in range(2, max(4, max_i + 1)):
        if n % i == 0:
            n_i += 2
    if max_i ** 2 == n:
        n_i -= 1
    list_n.append(n_i)

n_1 = []

for i in range(0, len(list_n) - 1):
    if list_n[i] == list_n[i+1]:
        print(i + 2, list_n[i], list_n[i+1])
        n_1.append(i + 2)
        count += 1

t_1 = time.time()

count_2 = 0
m_primes_previous = '0'

n_2 = []

for m in range(2, 10000):
    m_primes = []
    m_0 = m
    i = 0
    p_i = primes_1[i]
    max_p = int(m**0.5 + 1)

    while p_i < max_p:
        if m_0 % p_i == 0:
            m_primes.append(p_i)
            i = 0
            m_0 = m_0//p_i
            max_p = int(m_0**0.5 + 1)
        else:
            i += 1
            p_i = primes_1[i]
    if m_0 != 1:
        m_primes.append(m_0)

    m_primes_current = num_p_factors(m_primes)

    if m_primes_current == m_primes_previous:
        count_2 += 1
        print(m-1, m_primes_current, m_primes_previous)
        n_2.append(m-1)

    m_primes_previous = m_primes_current

t_2 = time.time()

print(t_1 - t_0, t_2 - t_1)

print(count, count_2, 's')

non_matches = (sorted(set(n_1) ^ set(n_2)))

for j in non_matches:
    j1_p_f = useful_functions.find_p_factors_ii(j)
    j2_p_f = useful_functions.find_p_factors_ii(j+1)
    print(j1_p_f, j2_p_f)