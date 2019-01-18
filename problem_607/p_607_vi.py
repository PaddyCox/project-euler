import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

d_mult = 1

d = (((100*d_mult)/2)**2 * 2)**0.5
n = 100*d_mult - d
d_i = d/5

print('d_i', d_i)

def m_solve(a, v):
    """Determine time taken to cross marsh with vertical displacement a, speed dx"""
    a *= d_mult
    return (((d_i - a)**2 + a**2)**0.5)/v

def dmc_solve(c, v):
    c *= d_mult
    return (2 * c + n) / (v * ((n + c) ** 2 + c ** 2) ** 0.5)

def n_solve(A, v):
    return (((n + A)**2 + A**2)**0.5)/v

def dm_solve(a, v):
    a *= d_mult
    return (2*a - d_i)/(v*((d_i - a)**2 + a**2)**0.5)

def a_solve(dm, v):
    return -(((dm * d_i * v)**2 / (4 * (2 - dm**2 * v**2)))**0.5 - d_i/2)

def c_solve(dm, v):
    return -((d_i**2 / (2 - dm**2 * v**2) - d_i**2 / 2)**0.5 - d_i / (2**0.5))/2**0.5

def dn_solve(A, v):
    A *= d_mult
    return (2*A + n)/(v*((n + A)**2 + A**2)**0.5)

dm_boundaries = [(dm_solve(0, i), dm_solve(d_i/2, i)) for i in range(5, 10)]

print(dm_boundaries)

print('c_boundary', [dmc_solve(x, 9) for x in range(8)])

for dm in range(111, 100, -1):
    print(dm, c_solve(dm/1000, 9))

print(dn_solve(0, 10), dn_solve(35, 10))

def block_feedback_solver():
    a_sum = 0
    a_guess = 20
    tolerance_target = 10**-12
    tolerance_actual  = 500
    iteration = 0
    dampening_factor = 1

    while abs(tolerance_actual) > tolerance_target and iteration <200:
        dn_i = dn_solve(a_guess, 10)
        a_guess = (a_guess - dampening_factor * (a_guess - a_sum))
        #print('dn_i', dn_i, 'tolerance_i', tolerance_actual)
        a_values = []
        for x, z in enumerate(dm_boundaries):
            if -dn_i > z[0] and -dn_i < z[1]:
                a_i = a_solve(-dn_i, x + 5)

                # print('#####', dn_i, x + 5, a_i)
            else:
                a_i = c_solve(dn_i, x + 5)
            a_values.append(a_i)

        a_sum = sum(a_values)
        tolerance_actual = a_guess - a_sum
        #print(iteration, a_guess, a_sum, dn_i)
        iteration += 1

    print('iterations: {}, dn/-dm: {}, a_values: {}'.format(iteration - 1, dn_i, a_values))
    return(a_values)

a_values = block_feedback_solver()

time_m = [m_solve(a_values[i], i + 5) for i in range(5)]
time_n = n_solve(sum(a_values), 10)

print(time_n, time_m, time_n + sum(time_m))


#for j in range(5, 10):
#   print(a_solve())