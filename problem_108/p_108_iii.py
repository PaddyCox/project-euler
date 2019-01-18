import time
from useful_functions import find_p_factors as fact_find
import fractions

time_0 = time.time()

def brute_num_n(n):
    total = 0
    n_fact = fact_find(n)
    for x in range(n + 1, n * 2 + 1):
        if (n * x) % (x - n) == 0:
            total += 1
            y = (n * x) // (x - n)
            c = x - n
            print(fact_find(n), x, y, c)
    return total

print(brute_num_n(35))

"""for j in range(9000, 10000):
    num_div = 0
    for i in range(1, int(j**0.5)):
        if j % i == 0:
            num_div += 2
    if j**0.5 % 1 == 0:
        num_div += 1
    num_n = brute_num_n(j)
    if num_n > 50:
        print(j, num_div, num_n, num_div/num_n)"""

print(time.time() - time_0)
