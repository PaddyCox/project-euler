# File becoming messy, clean start for testing at p_549_ii

import math
from useful_functions import rwh_primes

def to_base_10(n, b):
    str_n = str(n)
    for c in str(n):
        if int(c) >= b:
            print("All digits of n must be less than b:", "n:{}, b:{}".format(n, b))
            return None
    l = len(str(n))
    output = sum([b**(l - (i + 1)) * int(str_n[i]) for i in range(0, l)])
    return output

def recursive_multiplier(i, j, factors_i, m_i, p_i):
    count_j = factors_i.count(j)
    key_j = str(j) + '_' + str(count_j)
    print("TTTTT", i, key_j)
    if key_j in m_p_exp:
        check_m = m_p_exp[key_j]
    else:
        check_m = to_base_10(int(base_p_solution(count_j, j)[0]), j)
        m_p_exp[key_j] = check_m
    if not check_m:
        print(i, j, factors_i, m_i, p_i)
        exit()
    new_m = max(m_i, check_m)
    solutions_i[i] = new_m
    for z in range(p_i, l):
        p_z = primes_n[z]
        new_i = i * p_z
        if new_i > 10**2:
            print('skipped')
            return
        else:
            print('even one?')
            recursive_multiplier(i * p_z, p_z, factors_i + [p_z], new_m, z)

def base_p_solution(alpha, b):
    g_0 = alpha * (b - 1)
    a_max = int(math.log(g_0, b))
    a_max_check = str(b - 1) * a_max + '0'
    return_val = to_base_10(a_max_check, b)
    print("AAA", a_max_check, return_val)
    if return_val < alpha:
        a_max += 1
    print('a_max', a_max)
    remain_p = alpha
    total_b = 0
    chars = []
    b_powers = [b**j for j in range(a_max - 1, -1, -1)]
    # print('b_powers', b_powers)
    for i in range(a_max):
        #print(i, b_powers)
        i_mul = sum(b_powers[i:a_max])
        #print('i', i, i_mul, remain_p)
        i_char = remain_p // i_mul
        total_b += (i_char) * i_mul
        remain_p %= i_mul
        chars.append(i_char)

    if chars[-1] >= b:
        if len(chars) == 1:
            chars.insert(0, 1)
        elif chars[-2] == b - 1:
            chars[-2] = 0
            chars.insert(0, 1)
        else:
            chars[-2] += 1
        chars[-1] = 0

    chars.append(0)
    return (''.join(map(str, chars)), total_b)

def sum_i(i, b):
    l = len(str(i))
    return sum([b**(j) * (l - j) + int(str(i)[j]) for j in range(l - 1, -1, -1)])


print((base_p_solution(5, 2)))
print((base_p_solution(6, 2)))

print(to_base_10(int(base_p_solution(2, 2)[0]), 2))

print(to_base_10(int(base_p_solution(5, 2)[0]), 2))

primes_n = rwh_primes(10**8)

l = len(primes_n)

m_p_exp = {'2_1': 2}

solutions_i = {}




for e, p in enumerate(primes_n):
    if p > 10**2:
        break
    else:
        recursive_multiplier(p, p, [p], p, e)

print(len(solutions_i))

print(sum(solutions_i))

print(solutions_i)

print(m_p_exp)


