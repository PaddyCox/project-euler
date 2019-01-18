""" Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for
example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below
one-million that are not bouncy and only 277032 non-bouncy numbers below 1010.

How many numbers below a googol (10100) are not bouncy? """

import itertools
import operator
import functools
import math

n_i = 5

def ncr(n, r):
    r = min(r, n-r)
    numer = functools.reduce(operator.mul, range(n, n - r, -1), 1)
    denom = math.factorial(r)
    return numer//denom

def nbox_kball(n, k):
    i_0 = 1
    for num in range(k - n + 1, k):
        i_0 *= num
    for denom_0 in range(1, n):
        i_0 /= denom_0
    return int(i_0)



total_0 = 99

for digits in range(3, 101):
    unique_digits = min(digits, 10)
    des_sub_t = 0
    asc_sub_t = 0
    for case in range(2, min(11, unique_digits + 1)):
        sub_total_descending = ncr(10, case)
        combos = nbox_kball(case, digits)
        des_t = sub_total_descending * combos
        des_sub_t += des_t
    for case in range(2, min(10,unique_digits + 1)):
        sub_total_ascending = ncr(9, case)
        combos = nbox_kball(case, digits)
        asc_t = sub_total_ascending * combos
        asc_sub_t += asc_t
    total_0 += (asc_sub_t + des_sub_t)
    #print(asc_sub_t, des_sub_t, combos, digits, case)
    total_0 += 9

print(total_0)




