from useful_functions import rwh_primes
from useful_functions import find_p_factors_ii
import math

primes_1 = rwh_primes(10**4)

print(len(primes_1))

def two_groups(n):
    total = 1
    n_i = n
    last_term = 1
    for i in range(1, n//2 + 1):
        current_term = (last_term * (n + 1 - i)/i)/(int(2*i/n) + 1)
        total += current_term
        last_term = current_term
    return total

print(two_groups(5))

print(two_groups(4))

print(two_groups(3))

print(find_p_factors_ii(1000000009))

def a_choose_b(a, b):
    return (math.factorial(a)/(math.factorial(b) * math.factorial(a - b)))

print(a_choose_b(11, 5))

total_twos = 0

for a in range(1, 40):
    total_twos += (10**8/(2**a))
    print(total_twos)