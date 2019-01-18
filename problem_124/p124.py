import useful_functions
from collections import OrderedDict
from operator import itemgetter

def ordered_radical(n):
    o_r = 1
    unique_p_factors = set(useful_functions.find_p_factors(n))
    for i in unique_p_factors:
        o_r *= i
    return o_r

print(ordered_radical(8))
print(ordered_radical(504))

empty_dic = {}

for x in range(1, 100001):
    empty_dic[x] = ordered_radical(x)
