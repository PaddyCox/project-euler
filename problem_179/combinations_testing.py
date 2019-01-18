import itertools
import math

def factorial_reducer(n, i):
    return_product = 1
    for j in range(0, i):
        return_product *= (n - j)
    return_product /= math.factorial(i)
    print(math.factorial(n)/(math.factorial(n - i) * math.factorial(i)), return_product)
    return return_product

def combinator(n):
    return_total = 1
    if n % 2 == 0:
        for i in range(1, n//2):
            return_total += factorial_reducer(n, i)
        return_total += (factorial_reducer(n, n // 2)//2)
    else:
        for i in range(1, (n - 1)//2 + 1):
            return_total += factorial_reducer(n, i)
    return return_total

for z in range(1, 11):
    print(combinator(z))
