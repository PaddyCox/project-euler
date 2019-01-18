from useful_functions import rwh_primes
import time

max_n = 10**6
primes =  rwh_primes(max_n)
x_vals = {i for i in range(1, max_n + 1)}


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
                return sum(p_fact_n) - n
            p_i = next(p)
    return sum(p_fact_n) - n


t_0 = time.time()

cont_1 = True

while cont_1:
    try:
        n_i = x_vals.pop()
    except KeyError:
        cont_1 = False
        continue

    cont_2 = True
    list_chain = [n_i]
    while cont_2:
        n_j = all_factors(n_i)
        if n_j in list_chain:
            a_chain = list_chain[list_chain.index(n_j):]
            print('CHAIN', len(a_chain), min(a_chain), a_chain)
            cont_2 = False
        try:
            x_vals.remove(n_j)
            list_chain.append(n_j)
            n_i = n_j
        except KeyError:
            cont_2 = False


print(time.time() - t_0)


