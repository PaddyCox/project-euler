from useful_functions import find_p_factors_ii
from useful_functions import is_prime
from functools import reduce
from operator import mul
import copy
import collections
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


first_twenty_primes = []

c = 2
while len(first_twenty_primes) < 15:
    if is_prime(c):
        first_twenty_primes.append(c)
    c += 1

print(first_twenty_primes)

#prime_dict = {p: max(min(7 - i, 1), 0) for i, p in enumerate(first_twenty_primes)}

prime_dict = {2: 2, 3: 1, 5: 0, 7: 0, 11: 0, 13: 0, 17: 0, 19: 0, 23: 0, 29: 0, 31: 0, 37: 0}

print(prime_dict)

class Problem110:
    def __init__(self, dict_pf):
        self.dict_pf = dict_pf
        self.unique_factors = list(set(sorted([pf for pf in dict_pf if dict_pf[pf] != 0])))
        self.num_unique_factors = len(self.unique_factors)
        self.dict_pf_2 = {pf: self.dict_pf[pf] * 2 for pf in self.unique_factors}
        self.diophantine_solutions = 0
        self.max_n = reduce(mul, [x ** dict_pf[x] for x in dict_pf])

    def diophantine_reciprocals(self, pf_i, total):
        if total <= self.max_n:
            self.diophantine_solutions += 1
            for i in range(pf_i, self.num_unique_factors):
                current_pf = self.unique_factors[i]
                count_pf = self.dict_pf_2[current_pf]
                for j in range(1, count_pf + 1):
                    self.diophantine_reciprocals(i + 1, total * (current_pf ** j))

    def answer(self):
        self.diophantine_reciprocals(0, 1)

        return self.diophantine_solutions, self.max_n

#check = (Problem110({2: 11, 3: 7, 5: 4, 7: 2, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1, 29: 1, 31: 0, 37: 0, 41: 0, 43: 0, 47: 0}).answer())

#print(check[0], check[1], check[0]/check[1])

print(dict(collections.Counter(find_p_factors_ii(181948476645936000))))


print(Problem110(({2: 8, 3: 5, 5: 3, 7: 2, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1, 29: 1})).answer())

solution = 0
previous_solution = 0
previous_n = 1
dict_n_v_solutions = {}
while solution < 1000:
    min_p = 1000
    best_ratio = 0
    best_p = 'n/a'
    temp_solution = 0
    temp_n = 0
    for p in prime_dict:
        if prime_dict[p] < min_p:
            min_p = prime_dict[p]
            prime_dict[p] += 1
            prime_dict_2 = copy.copy(prime_dict)
            prime_dict_2[p] += 1
            p_ans = Problem110(prime_dict).answer()
            p_ans_2 = Problem110(prime_dict_2).answer()
            if p_ans[0] > 4000000:
                print(p_ans, {p: prime_dict[p] for p in prime_dict if prime_dict[p] > 0})
            if p_ans_2[0] > 4000000:
                print(p_ans_2, {p: prime_dict_2[p] for p in prime_dict_2 if prime_dict_2[p] > 0})
            p_ratio = (min(p_ans[0], 4000000) - previous_solution) / (p * previous_n - previous_n)
            if p_ratio > best_ratio:
                best_ratio = p_ratio
                best_p = p
                temp_solution = p_ans[0]
                temp_n = p_ans[1]
            prime_dict[p] -= 1
    previous_solution = temp_solution
    previous_n = temp_n
    solution = temp_solution
    prime_dict[best_p] += 1
    dict_n_v_solutions[previous_n] = previous_solution
    print('Iterative solution:', temp_solution, {p: prime_dict[p] for p in prime_dict if prime_dict[p] > 0}, reduce(mul, [x ** prime_dict[x] for x in prime_dict]))

print(find_p_factors_ii(180180))
print(dict_n_v_solutions)
print(solution, prime_dict, reduce(mul, [x ** prime_dict[x] for x in prime_dict]))

x = np.array([d for d in dict_n_v_solutions], dtype='int64')
y = np.array([dict_n_v_solutions[d] for d in dict_n_v_solutions], dtype='int64')
print(x)
print(y)
def func(x, a, b):
    return a * np.exp(b * x) + c

popt, pcov = (curve_fit(func, x, y))

plt.plot(x, func(x, *popt))
plt.show()





