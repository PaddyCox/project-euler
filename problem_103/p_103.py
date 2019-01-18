import itertools

import time

t_0 = time.time()

predicted_set_o = (22, 33, 40, 41, 42, 44, 47)


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

def recursive_sum_finder(a, b, running_total):
    sums = []
    if (a + 1) < b:
        for i in range(a + 1, b):
            sums.append(running_total + predicted_set[i])
            sums = sums + recursive_sum_finder(i, b, running_total + predicted_set[i])

    return sums


def total_sum_finder():
    subset_sums = []
    for l in range(0, 5):
        subset_sums += recursive_sum_finder(l, 7, predicted_set[l])
    return subset_sums

def check_set(list_1):
    set_1 = set(list_1)
    if len(set_1) == len(list_1):
        return True
    else:
        return False


for a, b, c, d, e, f, g in itertools.product(range(0, 6), range(0, 6), range(0, 6), range(0, 6), range(0, 6), range(0, 6), range(0, 6)):
    predicted_set = list(predicted_set_o)
    predicted_set[0] = predicted_set[0] - a
    predicted_set[1] = predicted_set[1] - b
    predicted_set[2] = predicted_set[2] - c
    predicted_set[3] = predicted_set[3] - d
    predicted_set[4] = predicted_set[4] - e
    predicted_set[5] = predicted_set[5] - f
    predicted_set[6] = predicted_set[6] - g
    if itertools_sum_check(predicted_set):
        print(predicted_set)
        print(sum(predicted_set))

print(time.time() - t_0)