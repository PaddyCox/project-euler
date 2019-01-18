from useful_functions import find_p_factors_ii

def brute_num_n(n):
    total = 0
    for x in range(n + 1, n * 2 + 1):
        if (n * x) % (x - n) == 0:
            total += 1
    return total

max_x = 0

for x in range(1, 10000):
    current_x = brute_num_n(x)
    if current_x > max_x:
        x_fact = find_p_factors_ii(x)
        print(x, current_x, x_fact)
        max_x = current_x

def recursive_num_fact(n, n_c, i_c):

    solution = 0
    p_fact_n = sorted(find_p_factors_ii(n) * 2)

    l_1 = len(p_fact_n)

    for i in range(0, l_1):


    return(p_fact_n)

print(recursive_num_fact(21))