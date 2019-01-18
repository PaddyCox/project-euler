import useful_functions
import time


start_time = time.time()

def ordered_radical(n):
    o_r = 1
    unique_p_factors = set(useful_functions.find_p_factors(n))
    for i in unique_p_factors:
        o_r *= i
    return o_r

print(ordered_radical(8))
print(ordered_radical(504))

list_ordered = []

for x in range(1, 100001):
    int_v = ordered_radical(x)
    len_x = len(str(x))
    num_zeroes = 6 - len_x
    string_n_or = str(int_v) + '.' + '0' * num_zeroes + str(x)
    float_n_or = float(string_n_or)
    list_ordered.append(float_n_or)

list_ordered.sort()

print(list_ordered)

print(list_ordered[9999])

print(time.time() - start_time)