import time
from useful_functions import find_p_factors as fact_find

time_0 = time.time()

def brute_num_n(n):
    total = 0
    n_fact = fact_find(n)
    for x in range(n + 1, n * 2 + 1):
        if (n * x) % (x - n) == 0:
            total += 1
            y = (n * x) // (x - n)
            x_fact = fact_find(x)
            y_fact = fact_find(y)
            xy_fact = fact_find(x*y)
            xandy_fact = fact_find(x+y)
            both_xandy = []
            just_x = []
            just_y = []
            for f in x_fact:
                if f in y_fact:
                    both_xandy.append(f)
                    y_fact.remove(f)
                else:
                    just_x.append(f)
            print(n_fact, xy_fact, both_xandy, just_x, y_fact)
    return total

print(brute_num_n(840))

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

