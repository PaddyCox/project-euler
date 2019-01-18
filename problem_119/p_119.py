import math

def root_check(i, max_p):
    d_p_s = []
    min_power = math.ceil(math.log(10, i))
    max_power = int(math.log(max_p, i))
    for j in range(min_power, max_power + 1):
        product = (i**j)
        sum_digits = sum([int(x) for x in str(product)])
        is_log = math.log(sum_digits, i)
        if is_log % 1 == 0 and is_log != 0:
            check_1 = j / is_log
            if check_1 % 1 == 0:
                print(i, j, product, sum_digits, check_1)
                d_p_s.append(product)
    return d_p_s

list_digit_power_sum = []

for n in range(2, 1000):
    list_digit_power_sum += root_check(n, 10**15)


set_solutions = sorted(set(list_digit_power_sum))

print(set_solutions)

print(len(set_solutions))