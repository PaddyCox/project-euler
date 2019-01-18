from useful_functions import rwh_primes
from functools import reduce
from operator import mul
import math
import time


def bisect_find(n, data):
    # Assign values to return if n is beyond range of data
    if n < data[0]:
        return 0
    max_p = data[-1]
    if n > max_p:
        return len(data) - 1

    l = len(data)
    lower_bound = 0
    upper_bound = l
    range_b = l

    # Loop over data until n is constrained by bounds
    while range_b > 1:
        mid_p = (lower_bound + upper_bound) //2
        if primes_i[mid_p] < n:
            lower_bound = mid_p
        else:
            upper_bound = mid_p
        range_b = upper_bound - lower_bound

    return upper_bound

def p_finder_ii(inverse_gradient, y_0=0, y_1=1):
    p = (inverse_gradient*(y_1 + 1)/(y_0 + 1))**(1/(y_1 - y_0))
    return p


sieve_p = rwh_primes(10**7)

max_p = 500500

primes_i = [sieve_p[i] for i in range(0, 500500)]

x_i = len(primes_i) * [0]

x_options = [127, 63, 31, 15, 7, 3, 1, 0]

dDdn_inverse = 10**6

I = 0
count = 0

while I != 500500:
    boundaries = []
    for i in range(len(x_options) - 1):
        boundaries.append(bisect_find(p_finder_ii(dDdn_inverse, x_options[i + 1], x_options[i]), primes_i))
    # print('log2 check', [(j + 1, boundaries[j + 1], x_options[j + 1], math.log2(x_options[j + 1] + 1)) for j in range(len(x_options) - 2)])
    i_values = [(boundaries[j + 1] - boundaries[j]) * int(math.log2(x_options[j + 1] + 1)) for j in range(0, len(x_options) - 2)]
    I = sum(i_values)
    dDdn_inverse += 2 * (500500 - I)
    count += 1
    # time.sleep(0.5)
    boundary_primes = [primes_i[b] for b in boundaries]
    print("Iteration", count, I, dDdn_inverse, boundaries, boundary_primes)

print(boundaries, I, dDdn_inverse)

base_500 = 0
answer_500 = 1

previous_x = 0
for e, x in enumerate(boundaries):
    for p in range(previous_x, x):
        # print(str(primes_i[p]) + '^' + str(x_options[-e]))
        answer_500 *= primes_i[p] ** (x_options[e])
        base_500 += answer_500 // 500500507
        answer_500 %= 500500507
    print('check_x', previous_x, x, primes_i[previous_x], primes_i[x], x_options[e])
    previous_x = x
    print(base_500, answer_500)

print("SUCCESS!!", len(str(base_500)), base_500 , answer_500)


