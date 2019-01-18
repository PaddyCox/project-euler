import math
from useful_functions import find_p_factors_ii
import operator
from functools import reduce
import time

t_0 = time.time()

def product(i):
    return reduce(operator.mul, i, 1)

max_c = 1000

sum_c = 0

for a in range(1, max_c//2):
    for b in range(a + 1, max_c - a):
        c = a + b
        if math.gcd(a, b) == 1:
            if math.gcd(a, c) == 1:
                if math.gcd(b, c) == 1:
                    pf_a = set(find_p_factors_ii(a))
                    pf_c = set(find_p_factors_ii(c))
                    rad_ab = product(pf_a) * product(pf_c)
                    if rad_ab < c:
                        pf_b = set(find_p_factors_ii(b))
                        if rad_ab * product(pf_b) < c:
                            print(a, b, c, pf_a, pf_b, pf_c)
                            sum_c += c

print(sum_c)

print(time.time() - t_0)
