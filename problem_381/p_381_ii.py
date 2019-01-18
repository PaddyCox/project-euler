import functools
import operator
import math
from useful_functions import rwh_primes
import time

def s_p(p):
    result = p
    for k in range(2, 5):
        result *= p - k
        result += 1
    result %= p
    # result *= p - 3
    for j in range(2, p - 4):
        result *= j
        result %= p
    return result

def s_p_ii(p):
    result = math.factorial(p-5)
    result %= p
    for i in range(p - 4, p - 2):
        result += result * i
        result %= p
    return result

t_0 = time.time()

primes_to_100 = rwh_primes(10**2)

primes_to_100.remove(2)
primes_to_100.remove(3)

t_1 = time.time()

s_p_i = [(p, s_p(p)) for p in primes_to_100]

t_2 = time.time()

s_p_ii = [(p, s_p_ii(p)) for p in primes_to_100]

t_3 = time.time()

total_1 = sum(list(zip(*s_p_i))[1])

total_2 = sum(list(zip(*s_p_ii))[1])

print(total_1, total_2)


print("Time calculate primes: {}s, time s_p_i: {}s, time s_p_ii: {}s".format(t_1 - t_0, t_2 - t_1, t_3 - t_2))