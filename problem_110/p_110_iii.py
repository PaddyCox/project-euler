from useful_functions import find_p_factors_ii
from useful_functions import is_prime
from functools import reduce
from operator import mul

first_twenty_primes = []

c = 2
while len(first_twenty_primes) < 20:
    if is_prime(c):
        first_twenty_primes.append(c)
    c += 1

print(first_twenty_primes)


n_test = reduce(mul, first_twenty_primes)

print(n_test)

def diophantine_reciprocals(pf_i, total):
    if total <= n:
        global diophantine_solutions
        diophantine_solutions += 1
        for i in range(pf_i, num_unique_factors):
            current_pf = unique_factors[i]
            count_pf = dic_pf[current_pf]
            for j in range(1, count_pf + 1):
                diophantine_reciprocals(i + 1, total * (current_pf ** j))

record_n = 0

for n in range(1260, 1261):
    diophantine_solutions = 0
    n_pfactors = find_p_factors_ii(n)
    n_squared_pf = sorted(n_pfactors * 2)
    unique_factors = sorted(list(set(n_pfactors)))
    num_unique_factors = len(unique_factors)
    dic_pf = {x: n_squared_pf.count(x) for x in unique_factors}
    diophantine_reciprocals(0, 1)
    if diophantine_solutions > record_n:
        record_n = diophantine_solutions
        print(n, diophantine_solutions, n_pfactors)




