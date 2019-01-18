import matplotlib.pyplot as plt
import copy
from useful_functions import find_p_factors_ii
import math
import scipy.optimize as opt
import numpy as np


initial_prime_dict = {2:1, 3:1, 5:0, 7:0, 11:0, 13:0, 17:0, 19:0, 23:0, 29:0, 31:0, 37:0, 43:0}


def di_sol(prime_dict):
    n = 1
    initial_sol = 1
    sum_a = []
    for d in prime_dict:
        if prime_dict[d] > 0:
            initial_sol *= 3
            initial_sol -= 1
            sum_a.append(prime_dict[d] - 1)
            n *= d ** prime_dict[d]
    for j in sum_a:
        initial_sol += j * (initial_sol - (initial_sol + 1)//3)
    return initial_sol, n

n_v_solution = []
n_v_best_solution = []

def prime_sol_increase(max_sol, dict_primes):
    current_n = 6
    current_s = 5
    copy_dict = dict_primes.copy()
    while current_s < max_sol:
        best_sol = 'N/A'
        other_sol = []
        best_dsdn = 0
        best_p = 'N/A'
        min_p = 100
        for p in copy_dict:
            if copy_dict[p] < min_p:
                min_p = copy_dict[p]
                copy_dict[p] += 1
                temp_s, temp_n = di_sol(copy_dict)
                other_sol.append((temp_n, temp_s))
                dsdn = ((temp_s - current_s) / (math.log((temp_n - current_n), 1.5)))
                print(dsdn)
                if dsdn > best_dsdn:
                    best_dsdn = dsdn
                    best_p = p
                    best_sol = (temp_n, temp_s)
                copy_dict[p] -= 1
            if copy_dict[p] == 0:
                break
        n_v_solution.extend(other_sol)
        n_v_best_solution.append(best_sol)
        current_n = best_sol[0]
        current_s = best_sol[1]
        copy_dict[best_p] += 1

    return current_s, current_n, copy_dict


print(prime_sol_increase(100000, initial_prime_dict))

zipped = (list(zip(*n_v_solution)))

x_data = np.array(zipped[0])

y_data = np.array(zipped[1])

plt.scatter(x_data, y_data, marker=".")

plt.scatter(*zip(*n_v_best_solution), c='r', marker='x')



min_n = 999999999
sol_n = 0

for i in n_v_solution:
    if i[1] > 4000000:
        print(i)
        if i[0] < min_n:
            print('best_i', i)
            min_n = i[0]
            sol_n = i[1]

print(min_n, sol_n)

value_check = find_p_factors_ii(30324746107656000)

value_check_2 = find_p_factors_ii(min_n)

dict_p_check = {p: value_check.count(p) for p in set(value_check)}

dict_p_check_2 = {p: value_check_2.count(p) for p in sorted(set(value_check_2))}

print(dict_p_check)
print(dict_p_check_2)

print(di_sol(dict_p_check))

def func(x, a, b, c, d):
    return a + b/(x**a) + c*(x**d)

popt, pcov = opt.curve_fit(func, x_data, y_data)

print("popt:", popt, "\npcov:", pcov)

plt.show()