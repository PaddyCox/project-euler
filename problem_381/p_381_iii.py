from useful_functions import rwh_primes
import time


def smart_381(p):
    p_mod_result = [(p - 1)//2]
    p_4 = p - 1
    while p_4 % 6 != 0:
        p_4 += p
    z = (p_4 // 6) % p
    p_mod_result.append(p - z)
    p_5 = p - z
    while p_5 % 4 != 0:
        p_5 += p
    y = (p_5 // 4) % p
    p_mod_result.append(p - y)
    return sum(p_mod_result) % p

t_0 = time.time()

set_n_primes = rwh_primes(10**8)

set_n_primes.remove(2)
set_n_primes.remove(3)

t_1 = time.time()

total_1 = 0

for prime in set_n_primes:
    sol_1 = smart_381(prime)
    total_1 += sol_1


print(total_1)

print(t_1 - t_0, time.time() - t_1)
