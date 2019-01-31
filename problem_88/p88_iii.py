import math
import time
from useful_functions import find_factors


def recurse_product_sum(s_target, p_target, x_p):
    #print('begin', s_target, p_target, x_p)
    if s_target == 0 and p_target == 1:
        return 1, True
    for i in range(x_p, s_target + 2):
        if p_target % i == 0:
            #print('stage_1', i, s_target, p_target, x_p)
            s_i = s_target // (i - 1)
            p_i = math.log(p_target, i)
            if s_i < p_i:
                break
            elif recurse_product_sum(s_target - (i - 1), p_target//i, i):
                return True
    #print('end')

def recurse_product_sum_ii(s_target, p_target, x_p):
    #print('begin', s_target, p_target, x_p)
    if s_target == 0 and p_target == 1:
        return True
    for i in range(x_p, max_i):
        x_i = factors_x[i]
        s_i = s_target // (x_i - 1)
        try:
            p_i = math.log(p_target, x_i)
        except ValueError:
            print(p_target, x_i)
            exit()

        if s_i < p_i:
            break
        elif recurse_product_sum_ii(s_target - (x_i - 1), p_target//x_i, i):
            return True
    #print('end')

set_n = set()

t_0 = time.time()

for k in range(2, 1200):
    k_0 = k + int(math.log(k, 2))
    for x in range(k_0, 2*k + 1):
        print(k, x)
        factors_x = sorted(list(find_factors(x)))
        max_i = len(factors_x)
        if recurse_product_sum_ii(x - k, x, 2):
            #print(k, x)
            set_n.add(x)
            break
#print(set_n)
print(sum(set_n))
print(time.time() - t_0)