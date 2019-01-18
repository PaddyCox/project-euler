import itertools
import math


def subset_sum_meta_test(list_2):
    length_num = len(list_2)
    total = 0
    combinations = itertools.combinations(list_2[1:], length_num//2 - 1)
    for combo in combinations:
        tally = 1
        for num in range(2, length_num + 1):
            if num in combo:
                tally += 1
            else:
                tally -= 1
            if tally < 0:
                total += 1
                break
    return total



def itertools_sum_check(list_1):
    list_1.sort()
    number_items = len(list_1)
    set_list = set(list_1)

    if len(set_list) != number_items:
        return False

    check_up_to = number_items // 2
    lower_half = (number_items + 1) // 2
    large_sum = sum(list_1[0:lower_half])
    small_sum = sum(list_1[:(-lower_half):-1])

    if large_sum <= small_sum:
        return False

    subset_sum = set()

    for i in range(1, check_up_to + 1):
        i_combos = itertools.combinations(list_1, i)
        for c_i in i_combos:
            sum_c = sum(c_i)
            if sum_c in subset_sum:
                return False
            subset_sum.add(sum_c)
    return True

sum1 = 0

for i in range(4, 14, 2):
    x_list = [x for x in range(1, i + 1)]
    x_sum = subset_sum_meta_test(x_list)
    factorial_x = (math.factorial(12)/(math.factorial(i)*math.factorial(12 - i)))
    x_sum_2 = x_sum * factorial_x
    print(i, x_sum, x_sum_2)
    sum1 += x_sum_2

print(sum1)