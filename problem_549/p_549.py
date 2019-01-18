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

def to_base_b(n, b):
    output = ''
    str_n = str(n)
    n_remain = n
    l = int(math.log(n, b))
    for d in range(l, -1, -1):
        output = output + str(n_remain//(b**d))
        n_remain %= (b**d)
    return int(output)

print(to_base_10(1000, 3))
print(to_base_10(14530, 7))
z = (to_base_10(10000, 7))

print(z)

print(to_base_b(z, 7))
print(to_base_b(4697, 7))
test = to_base_b(4697, 7)

print(test)
def guess_zero(p, alpha):
    return alpha * (p - 1)

def alpha_max(p, g0):
    return int(math.log(g0, p))

def base_p_solution(alpha, b):
    g_0 = alpha * (b - 1)
    a_max = int(math.log(g_0, b))
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
        else:
            chars[-2] += 1
        chars[-1] = 0

    chars.append(0)
    return (''.join(map(str, chars)), total_b)

def sum_i(i, b):
    l = len(str(i))
    return sum([b**(j) * (l - j) + int(str(i)[j]) for j in range(l - 1, -1, -1)])



print(to_base_10(int(base_p_solution(675, 7)[0]), 7))
print(base_p_solution(500, 2))
print(to_base_10(int(base_p_solution(500, 2)[0]), 2))
print(to_base_10(int(base_p_solution(2, 2)[0]), 2))

primes_n = rwh_primes(10**8)

l = len(primes_n)

m_p_exp = {'2_1': 2}

solutions_i = {}

def recursive_multiplier(i, j, factors_i, m_i, p_i):
    count_j = factors_i.count(j)
    key_j = str(j) + '_' + str(count_j)
    print("TTTTT", i, key_j)
    if key_j in m_p_exp:
        check_m = m_p_exp[key_j]
    else:
        check_m = to_base_10(int(base_p_solution(count_j, j)[0]), j)
        m_p_exp[key_j] = check_m
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


for e, p in enumerate(primes_n):
    if p > 10**2:
        break
    else:
        recursive_multiplier(p, p, [p], p, e)

print(len(solutions_i))

print(sum(solutions_i))

print(solutions_i)

print(m_p_exp)


