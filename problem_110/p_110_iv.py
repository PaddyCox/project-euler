from useful_functions import find_p_factors_ii
from useful_functions import is_prime
from functools import reduce
from operator import mul
import copy

first_twenty_primes = []

c = 2
while len(first_twenty_primes) < 20:
    if is_prime(c):
        first_twenty_primes.append(c)
    c += 1

print(first_twenty_primes)


n_test = reduce(mul, first_twenty_primes)

print(n_test)

iteritive_solution = {x: 0 for x in first_twenty_primes}

iteritive_solution[2] = 1
iteritive_solution[3] = 1

record_n = 6

max_prime_i = 0

diophantine_solutions = 0
best_di = 0
def diophantine_reciprocals(n, pf_i, total, num_unique_factors, unique_factors, dic_pf):
    if total <= n:
        global diophantine_solutions
        diophantine_solutions += 1
        for i in range(pf_i, num_unique_factors):
            current_pf = unique_factors[i]
            count_pf = dic_pf[current_pf]
            for j in range(1, count_pf + 1):
                diophantine_reciprocals(n, i + 1, total * (current_pf ** j), num_unique_factors, unique_factors, dic_pf)

def four_mil_solutions():
    global diophantine_solutions
    best_ratio = 0
    best_p = 0
    current_multiplier = 1
    zero_condition = False
    i_p = 0
    while not zero_condition:
        p = first_twenty_primes[i_p]
        if iteritive_solution[p] < current_multiplier:
            current_multiplier = iteritive_solution[p]
            if iteritive_solution[p] == 0:
                zero_condition = True
            temp_dic = copy.copy(iteritive_solution)
            temp_dic[p] += 1
            unique_factors = sorted(list(set([y for y in first_twenty_primes if iteritive_solution[y] > 0] + [p])))
            num_unique_factors = len(unique_factors)
            for p_factor in unique_factors:
                temp_dic[p_factor] = temp_dic[p_factor] * 2
            temp_n = record_n * p
            diophantine_reciprocals(temp_n, 0, 1, num_unique_factors, unique_factors, temp_dic)
            p_ratio = diophantine_solutions/temp_n
            if p_ratio > best_ratio:
                best_p = p
                best_di = diophantine_solutions
        diophantine_solutions = 0
    iteritive_solution[best_p] += 1
    print(iteritive_solution)


while best_di < 1000:
    four_mil_solutions()
    print(iteritive_solution, best_di)





