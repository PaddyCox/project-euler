import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

d_mult = 1

d = (((100*d_mult)/2)**2 * 2)**0.5
n = 100*d_mult - d
d_i = d/5

print('sqrt check', sqrt(10))

def m_solve(a, v):
    """Determine time taken to cross marsh with vertical displacement a, speed dx"""
    a *= d_mult
    return (((d_i - a)**2 + a**2)**0.5)/v

def dm_solve(a, v):
    a *= d_mult
    return (2*a - d_i)/(v*((d_i - a)**2 + a**2)**0.5)

def a_solve(dm, v):
    return 1 / sqrt(2) * (sqrt(d_i**2 / (2 - (dm)**2 * (v)**2) - (d_i**2) / 2) - d_i / (sqrt(2)))

def dn_solve(A, v):
    A *= d_mult
    return (2*A + n)/(v*((n + A)**2 + A**2)**0.5)

dm_boundaries = [(dm_solve(0, i), dm_solve(d/10, i)) for i in range(5, 10)]

print(dm_boundaries)

a_guess = 20
tolerance_target = 10**-6
tolerance_actual  = 500
iteration = 0

for dm_check in range(7, 10):
    for v_check in range(5, 10):
        print(- dm_check / 10, v_check, a_solve( - dm_check/10, v_check))



while abs(tolerance_actual) > tolerance_target:
    dn_i = dn_solve(a_guess, 10)
    print('dn_i', dn_i)
    a_sum = 0
    for x, z in enumerate(dm_boundaries):
        if -dn_i > z[0] and -dn_i < z[1]:
            a_sum += a_solve(dn_i, x + 5)

    print(iteration, a_guess, a_sum, dn_i)
    tolerance_actual = a_guess - a_sum
    a_guess = (a_guess + a_sum)/2
    iteration += 1


#for j in range(5, 10):
#   print(a_solve())