import math
import timeit
from useful_functions import find_p_factors_ii

print(timeit.timeit("for n in range(100): sqrt(n)", setup="from math import sqrt", number=1000))
print(timeit.timeit("for n in range(100): n**0.5", number=1000))
print(timeit.timeit("for n in range(1, 100): (n/2) % 1 == 1", number=100))
print(timeit.timeit("for n in range(1, 100): n/2 == int(n)", number=100))

def b_1(b):
    return 5*(b**2) + 8*b + 4

def b_2(b):
    return 5*(b**2) - 8*b + 4



for b in range(2, 10000000):
    L_1 = (math.sqrt(b_1(b)))/2
    L_2 = (math.sqrt(b_2(b)))/2
    if L_1 % 1 == 0:
        print('L_1', b, b + 1, L_1)
        print('pf', find_p_factors_ii(b), find_p_factors_ii(b + 1), find_p_factors_ii(L_1))
    if L_2 % 1 == 0:
        print('L_2', b, b - 1, L_2)
        print('pf', find_p_factors_ii(b), find_p_factors_ii(b - 1), find_p_factors_ii(L_2))


print(b_1(16), b_2(16))