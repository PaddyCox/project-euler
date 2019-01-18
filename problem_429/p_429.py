import math
import collections
from useful_functions import recursive_prime_factors
from useful_functions import rwh_primes

def flatten(l):
    # requires collections
    # potentially tripped up by strings
    output = []
    for el in l:
        if isinstance(el, collections.Iterable):
            for sub in flatten(el):
                output.append(sub)
        else:
            output.append(el)
    return output


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    else:
        return True

#note math module has gcd function (math.gcd(a, b))

def gcd_1(a, b):
    c = min(a, b)
    d = max(a, b)
    if d % c == 0:
        return False
    for i in range(2,  int(c ** 0.5) + 1):
        f2 = c/i
        if f2 % 1 == 0:
            if d % f2 == 0 or d % i == 0:
                return False
    return True


def unitary_divisor_finder(n):
    list_to_return = [(1, n)]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            i2 = n // i
            if gcd_1(i, i2):
                list_to_return.append((i, i2))
    return list_to_return


for x in range(2, 15):
    fact_x = math.factorial(x)
    results = unitary_divisor_finder(fact_x)
    print('\n')
    print(x, sum([j**2 for j in flatten(results)]), recursive_prime_factors(fact_x))
    print(len(results))
    for y in results:
        print(y[0], y[1], is_prime(y[0]), is_prime(y[1]))

primes_less_than_100mil = rwh_primes(100000000)

print(len(primes_less_than_100mil))

print(gcd_1(3, 240))

"""Unitary divisor pairs of N! are equal to number of ways to divide primes <= N into groups of two"""

# Find how many 2's in prime factors of factorial(10^8)

upper_limit_exponent = int(math.log(100000000, 2))

print(upper_limit_exponent)

total_twos = 0

for a in range(1, upper_limit_exponent + 1):
    iterative_twos = a * 100000000 // (2 ** a)
    total_twos += iterative_twos

print(total_twos)